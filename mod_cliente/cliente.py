from flask import Blueprint, render_template

from mod_login.login import validaSessao
from mod_cliente.clienteBD import Cliente

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder='templates')

@bp_cliente.route("/")
@validaSessao
def formListaClientes():
    cliente = Cliente()
    _clientes = cliente.selectAll()
    return render_template('formListaClientes.html', clientes = _clientes)

@bp_cliente.route("/formCliente")
@validaSessao
def formCliente():
    return render_template('formCliente.html')

@bp_cliente.route("/formEditCliente")
@validaSessao
def formEditCliente():
    return render_template('formCliente.html')

