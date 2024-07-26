from flask import Blueprint, render_template, redirect, url_for, flash
from .models import User, Car, Invoice, Budget
from .forms import AltaCocheForm, AltaClienteForm, FacturaForm, FacturaProformaForm, PresupuestoForm
from . import db

# Crear el blueprint 'main'
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
        new_cliente = User(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            dni=form.dni.data,
            direccion=form.direccion.data,
            telefono=form.telefono.data,
            email=form.email.data
            # Asegúrate de manejar la carga de archivos aquí si es necesario
        )
        db.session.add(new_cliente)
        db.session.commit()
        flash('Cliente dado de alta correctamente.')
        return redirect(url_for('main.index'))
    return render_template('alta_cliente.html', form=form)

@main.route('/transferir_coche', methods=['GET', 'POST'])
def transferir_coche():
    return render_template('transferir_coche.html')

@main.route('/dar_baja_coche', methods=['GET', 'POST'])
def dar_baja_coche():
    return render_template('dar_baja_coche.html')

@main.route('/matricular_coche', methods=['GET', 'POST'])
def matricular_coche():
    return render_template('matricular_coche.html')

@main.route('/consultar_dgt', methods=['GET', 'POST'])
def consultar_dgt():
    return render_template('consultar_dgt.html')

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
