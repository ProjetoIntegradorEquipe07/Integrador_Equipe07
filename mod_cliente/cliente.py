from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from mod_login.login import validaSessao, validaGrupo
from mod_cliente.clienteBD import Cliente
from funcoes import Funcoes

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder='templates')

@bp_cliente.route("/")
@validaSessao
@validaGrupo
def formListaClientes():
    cliente = Cliente()
    _clientes = cliente.selectAll()
    return render_template('formListaClientes.html', clientes = _clientes)

@bp_cliente.route("/formCliente")
@validaSessao
@validaGrupo
def formCliente():
    cliente = Cliente()
    return render_template('formCliente.html', cliente=cliente)

@bp_cliente.route("/formEditCliente", methods=['POST'])
@validaSessao
@validaGrupo
def formEditCliente():
    cliente = Cliente()
    cliente.id_cliente = request.form['id_cliente']
    cliente.selectOne()
    return render_template('formCliente.html', cliente=cliente)

@bp_cliente.route("/addCliente", methods=['POST'])
@validaSessao
@validaGrupo
def addCliente():
    _mensagem = ""
    try:
        _nome = request.form['nome']
        _cpf = request.form['cpf']
        _telefone = request.form['telefone']
        _compra_fiado = request.form['compra_fiado']
        _senha = Funcoes.criptografaSenha(request.form['senha'])
        _dia_fiado = request.form['dia_fiado']

        cliente = Cliente(0,_nome,_cpf,_telefone,_compra_fiado,_senha,_dia_fiado)
        _mensagem = cliente.insert()

        return jsonify(erro = False, mensagem = _mensagem)
    except Exception as e:
        _mensagem_erro, _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem_erro, mensagem_exception = _mensagem_exception)

@bp_cliente.route("/editCliente", methods=['POST'])
@validaSessao
@validaGrupo
def editCliente():
    _mensagem = ""
    try:
        _id_cliente = request.form['id_cliente']
        _nome = request.form['nome']
        _cpf = request.form['cpf']
        _telefone = request.form['telefone']
        _compra_fiado = request.form['compra_fiado']
        _senha = ""
        _dia_fiado = request.form['dia_fiado']

        cliente = Cliente(_id_cliente,_nome,_cpf,_telefone,_compra_fiado,_senha,_dia_fiado)
        _mensagem = cliente.update()

        return jsonify(erro = False, mensagem  = _mensagem)
    except Exception as e:
        _mensagem_erro, _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem_erro, mensagem_exception = _mensagem_exception)

@bp_cliente.route("/deleteCliente", methods=['POST'])
@validaSessao
@validaGrupo
def deleteCliente():
    _mensagem = ""
    try:
        cliente = Cliente()
        cliente.id_cliente = request.form['id_cliente']

        _mensagem = cliente.delete()

        return jsonify(erro = False, mensagem = _mensagem)
    except Exception as e:
        _mensagem_erro, _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem_erro, mensagem_exception = _mensagem_exception)