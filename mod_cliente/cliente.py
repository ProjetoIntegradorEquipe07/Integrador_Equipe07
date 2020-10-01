from flask import Blueprint, render_template

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder='templates')

@bp_cliente.route("/")
def formListaClientes():
    return render_template('formListaClientes.html')

@bp_cliente.route("/formCliente")
def formCliente():
    return render_template('formCliente.html')