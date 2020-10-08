from flask import Blueprint, render_template, request, redirect, url_for

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
    cliente = Cliente()
    return render_template('formCliente.html', cliente=cliente)

@bp_cliente.route("/formEditCliente")
@validaSessao
def formEditCliente():
    cliente = Cliente()
    cliente.selectOne()
    return render_template('formCliente.html', cliente=cliente)

@bp_cliente.route("/addCliente", methods=['POST'])
@validaSessao
def addCliente():
    _nome = request.form['nome']
    _cpf = request.form['cpf']
    _telefone = request.form['telefone']
    _compra_fiado = request.form['compra_fiado']
    _senha = request.form['senha']
    _dia_fiado = request.form['dia_fiado']

    cliente = Cliente(0,_nome,_cpf,_telefone,_compra_fiado,_senha,_dia_fiado)
    cliente.insert()

    return redirect(url_for('cliente.formListaClientes'))
