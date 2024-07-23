from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class AltaCocheForm(FlaskForm):
    license_plate = StringField('Matrícula', validators=[DataRequired(), Length(min=1, max=20)])
    brand = StringField('Marca', validators=[DataRequired(), Length(min=1, max=50)])
    model = StringField('Modelo', validators=[DataRequired(), Length(min=1, max=50)])
    owner_id = IntegerField('ID del Propietario', validators=[DataRequired()])
    submit = SubmitField('Dar de Alta')

class AltaClienteForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=1, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=1, max=150)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=1, max=150)])
    submit = SubmitField('Dar de Alta')

class FacturaForm(FlaskForm):
    date = StringField('Fecha', validators=[DataRequired()])
    amount = FloatField('Monto', validators=[DataRequired()])
    client_id = IntegerField('ID del Cliente', validators=[DataRequired()])
    details = TextAreaField('Detalles', validators=[DataRequired()])
    submit = SubmitField('Crear Factura')

class FacturaProformaForm(FlaskForm):
    date = StringField('Fecha', validators=[DataRequired()])
    amount = FloatField('Monto', validators=[DataRequired()])
    client_id = IntegerField('ID del Cliente', validators=[DataRequired()])
    details = TextAreaField('Detalles', validators=[DataRequired()])
    submit = SubmitField('Crear Factura Proforma')

class PresupuestoForm(FlaskForm):
    date = StringField('Fecha', validators=[DataRequired()])
    amount = FloatField('Monto', validators=[DataRequired()])
    client_id = IntegerField('ID del Cliente', validators=[DataRequired()])
    details = TextAreaField('Detalles', validators=[DataRequired()])
    submit = SubmitField('Crear Presupuesto')
