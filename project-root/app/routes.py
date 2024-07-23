from flask import Blueprint, render_template, redirect, url_for
from .models import User, Car, Invoice, Budget
from .forms import AltaCocheForm, AltaClienteForm, FacturaForm, FacturaProformaForm, PresupuestoForm
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/alta_coche', methods=['GET', 'POST'])
def alta_coche():
    form = AltaCocheForm()
    if form.validate_on_submit():
        new_car = Car(
            license_plate=form.license_plate.data,
            brand=form.brand.data,
            model=form.model.data,
            owner_id=form.owner_id.data
        )
        db.session.add(new_car)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('alta_coche.html', form=form)

@main.route('/alta_cliente', methods=['GET', 'POST'])
def alta_cliente():
    form = AltaClienteForm()
    if form.validate_on_submit():
        new_client = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('alta_cliente.html', form=form)

@main.route('/facturacion', methods=['GET', 'POST'])
def facturacion():
    form = FacturaForm()
    if form.validate_on_submit():
        new_invoice = Invoice(
            date=form.date.data,
            amount=form.amount.data,
            client_id=form.client_id.data,
            details=form.details.data
        )
        db.session.add(new_invoice)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('facturacion.html', form=form)

@main.route('/facturas_proforma', methods=['GET', 'POST'])
def facturas_proforma():
    form = FacturaProformaForm()
    if form.validate_on_submit():
        new_invoice = Invoice(
            date=form.date.data,
            amount=form.amount.data,
            client_id=form.client_id.data,
            details=form.details.data
        )
        db.session.add(new_invoice)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('facturas_proforma.html', form=form)

@main.route('/presupuestos', methods=['GET', 'POST'])
def presupuestos():
    form = PresupuestoForm()
    if form.validate_on_submit():
        new_budget = Budget(
            date=form.date.data,
            amount=form.amount.data,
            client_id=form.client_id.data,
            details=form.details.data
        )
        db.session.add(new_budget)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('presupuestos.html', form=form)

# Añade más rutas según sea necesario
