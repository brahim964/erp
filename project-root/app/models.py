from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    cars = db.relationship('Car', backref='owner', lazy=True)
    invoices = db.relationship('Invoice', backref='client', lazy=True)
    budgets = db.relationship('Budget', backref='client', lazy=True)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    details = db.Column(db.Text, nullable=False)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    details = db.Column(db.Text, nullable=False)
