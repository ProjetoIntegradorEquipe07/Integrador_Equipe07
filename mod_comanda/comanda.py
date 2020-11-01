from flask import Blueprint, render_template, request, url_for, jsonify, session, json
import datetime

from mod_login.login import validaSessao, validaGrupo
from mod_comanda.comandaBD import Comanda
from mod_comanda.comandaProdutoBD import ComandaProduto
from mod_produto.produtoBD import Produto



bp_comanda = Blueprint('comanda', __name__, url_prefix='/comanda', template_folder='templates')

@bp_comanda.route("/")
@validaSessao
def formListaComandas():
    return render_template('formListaComandas.html')

@bp_comanda.route("/dashboard", methods = ['GET', 'POST'])
@validaSessao
@validaGrupo
def dashboard():
    comanda = Comanda()
    _comandas_abertas = comanda.contaComandasPorStatus(0)
    _recebimentos_a_vista = comanda.contaRecebimentosPorTipo(1)
    return render_template('dashboard.html', comandas_abertas = _comandas_abertas, recebimentos_a_vista = _recebimentos_a_vista)

@bp_comanda.route("/buscaComandasPorStatus", methods = ['POST'])
@validaSessao
def buscaComandasPorStatus():
    try:
        _comanda = Comanda()
        _comanda.status_comanda = request.form['status_comanda']
        _lista = _comanda.selectComandaByStatus()
        return jsonify(erro = False, comandas = _lista)
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_comanda.route('/buscaRecebimentosPorTipo', methods = ['POST'])
@validaSessao
def buscaRecebimentosPorTipo():
    try:
        _comanda = Comanda()
        _tipo = request.form['tipo']
        _lista = _comanda.selectRecebimentosPorTipo(_tipo)
        return jsonify(erro = False, comandas = _lista)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
    


@bp_comanda.route("/formListaComandasAbertas", methods = ['POST'])
@validaSessao
@validaGrupo
def formListaComandasAbertas():
    _comanda = Comanda()
    _comanda.status_comanda = 0
    _lista = _comanda.selectComandaByStatus()

    return render_template('formListaComandasAbertas.html', lista = _lista)


@bp_comanda.route("/addComanda", methods=['POST'])
@validaSessao
def addComanda():
    try:
        comanda = Comanda()
        comanda.comanda = request.form['comanda']
        comanda.data_hora = datetime.datetime.now()
        comanda.status_pagamento = 0
        comanda.status_comanda = 0
        comanda.funcionario_id = session['id']

        _mensagem = comanda.insertNumeroComanda()

        return jsonify(erro = False, mensagem = _mensagem)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)


@bp_comanda.route("/formAddProdutoComanda", methods=['POST'])
@validaSessao
def formAddProdutoComanda():
    _comanda = ComandaProduto()
    _produto = Produto()
    _lista_produto = _produto.selectAll()
    _comanda.comanda_id = request.form['id_comanda']
    comanda_aux = _comanda.selectOneComanda()    
    return render_template('formComanda.html', comanda = comanda_aux, lista_produto = _lista_produto)

@bp_comanda.route("/addProdutoComanda", methods=['POST'])
@validaSessao
def addProdutoComanda():
    try:
        _comanda_produto = ComandaProduto()
        _produto = Produto()
        _produto.id_produto = request.form['id_produto']
        _produto.selectOne()
        _comanda_produto.funcionario_id = session['id']
        _comanda_produto.produto_id = request.form['id_produto']
        _comanda_produto.comanda_id = request.form['id_comanda']
        _comanda_produto.quantidade = request.form['quantidade']
        _comanda_produto.valor_unitario = _produto.valor_unitario

        _mensagem = _comanda_produto.insertProdutoComanda()

        return jsonify(erro = False, mensagem = _mensagem)


    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_comanda.route("/validaComanda", methods=['POST'])
@validaSessao
def validaComanda():
    try:
        _comanda = Comanda()
        _comanda.comanda = request.form['valor']
        _comanda.status_comanda = 0
        _resultado = _comanda.verificaSeComandaExiste()

        if len(_resultado) > 0:
            return jsonify(input_existe = True)
        else:
            return jsonify(input_existe = False)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_comanda.route("/buscaNumeroComanda", methods = ['POST'])
@validaSessao
def buscaNumeroComanda():
    try:
        _comanda = Comanda()
        _comanda.comanda = request.form['comanda']
        _comanda.status_comanda = 0
        _comanda_aux = _comanda.selectComandaByNumero()
        _produtos_comanda = _comanda.selectProdutosPorNumeroComanda()

        return jsonify(erro = False, comanda = _comanda_aux, produtos = _produtos_comanda)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception) 