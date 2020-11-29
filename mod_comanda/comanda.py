from flask import Blueprint, render_template, request, url_for, jsonify, session, json, redirect, send_file
import datetime
import decimal
import os

from mod_login.login import validaSessao, validaGrupo
from mod_comanda.comandaBD import Comanda
from mod_comanda.comandaProdutoBD import ComandaProduto
from mod_produto.produtoBD import Produto
from mod_cliente.clienteBD import Cliente
from funcoes import Funcoes
from geraPDF import PDF



bp_comanda = Blueprint('comanda', __name__, url_prefix='/comanda', template_folder='templates')

@bp_comanda.route("/")
@validaSessao
def formListaComandas():
    return render_template('formListaComandas.html')

@bp_comanda.route("/formListaFiados", methods = ['GET', 'POST'])
@validaSessao
def formListaFiados():
    return render_template('formListaFiados.html')



@bp_comanda.route("/dashboard", methods = ['GET', 'POST'])
@validaSessao
@validaGrupo
def dashboard():
    comanda = Comanda()
    _comandas_abertas = comanda.contaComandasPorStatus(0)
    _recebimentos_a_vista = comanda.contaRecebimentosPorTipo(1)
    _recebimentos_fiado = comanda.contaRecebimentosPorTipo(2)
    _comandas_em_atraso = len(comanda.selectComandasEmAtraso())
    return render_template('dashboard.html', comandas_abertas = _comandas_abertas, recebimentos_a_vista = _recebimentos_a_vista, recebimentos_fiado = _recebimentos_fiado, comandas_em_atraso = _comandas_em_atraso)

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

@bp_comanda.route("/buscaComandasEmAtraso", methods = ['POST'])
@validaSessao
def buscaComandasEmAtraso():
    try:
        _comanda = Comanda()        
        result = _comanda.selectComandasEmAtraso()

        return jsonify(erro = False, comandas = result)
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
        cliente = Cliente()
        cliente.cpf = request.form['cpf'].replace('.','').replace('-','')
        cliente.buscaClientePorCPF()
        comanda.cliente_id = cliente.id_cliente

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
            _mensagem = 'Erro no banco controller'
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

@bp_comanda.route("/deletaProdutoComanda", methods = ['POST'])
@validaSessao
def deletaProdutoComanda():
    try:
        _comanda_produto = ComandaProduto()

        _comanda_produto.id_comanda_produto = request.form['id_comanda_produto']

        _mensagem = _comanda_produto.deleteProdutoComanda()

        return jsonify(erro = False, mensagem = _mensagem)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
    
@bp_comanda.route("/formFechaComanda", methods = ['POST'])
@validaSessao
def formFechaComanda():
    _comanda = ComandaProduto()
    _comanda.comanda_id = request.form['id_comanda']
    comanda_aux = _comanda.selectOneComanda()
    return render_template('formFechaComanda.html', comanda = comanda_aux)

@bp_comanda.route("/fechaComanda", methods = ['POST'])
@validaSessao
def fechaComandaAVista():
    try:
        _comanda = Comanda()
        _comanda.id_comanda = request.form['id_comanda']
        _comanda.status_pagamento = 1
        _comanda.status_comanda = 1
        _valor_total = request.form['valor_total']
        desconto = request.form['valor_desconto']
        _valor_final = request.form['valor_final']
        _funcionario_id = session['id']
        _valor_desconto = 0 if desconto == "" else desconto
        _mensagem, _id_recebimento = _comanda.fechaComanda(_valor_final, _valor_total, _valor_desconto, datetime.datetime.now(),1, _funcionario_id)

        return jsonify(erro = False, mensagem = _mensagem, id_recebimento = _id_recebimento)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_comanda.route("/registraComandaFiado", methods = ['POST'])
@validaSessao
def registraComandaFiado():
    try:
        _cliente = Cliente()
        _cliente.cpf = request.form['cpf']
        _cliente.senha = Funcoes.criptografaSenha(request.form['senha']) 
        compra_fiado = True if len(_cliente.validaClienteFiado()) > 0 else False

        if compra_fiado:
            result = _cliente.validaSenhaCliente()
            senha_correta = True if len(result) > 0 else False
            if senha_correta:
                _comanda = Comanda()
                _comanda.id_comanda = request.form['id_comanda']
                _comanda.status_comanda = 2
                _comanda.data_assinatura_fiado = datetime.datetime.now()
                _comanda.cliente_id = result[0]
                _mensagem = _comanda.registraComandaFiado()

                return jsonify(erro = False, mensagem = _mensagem)
            else:
                 _mensagem = 'Senha incorreta!'
            return jsonify(erro = True, mensagem = _mensagem)
        else:
            _mensagem = 'Cliente não está registrado para fiado!'
            return jsonify(erro = True, mensagem = _mensagem)
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_comanda.route("/buscaFiadoPorCliente", methods = ['POST'])
@validaSessao
def buscaFiadoPorCliente():
    try:
        _comanda = Comanda()
        _cliente = Cliente()
        _cliente.cpf = request.form['cpf_cliente'].replace('-','').replace('.','')
        _cliente_encontrado = _cliente.buscaClientePorCPF()
        if _cliente_encontrado:
            
            _comanda.status_comanda = 2           
            
            _tupla_fiados = _comanda.buscaFiadosPorCliente(_cliente.id_cliente)      
            return jsonify(erro = False,cliente_encontrado = True, fiados = _tupla_fiados)
        else:
            return jsonify(erro = False, cliente_encontrado = False)
        
    
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_comanda.route("/recebeFiado", methods = ['POST'])
@validaSessao
def recebeFiado():
    try:
        _id_comandas = request.form.getlist('id_comandas')[0].split(",")
        _valor_final = request.form['valor_final']
        _valor_total = request.form['valor_total']
        desconto = request.form['desconto']
        _valor_desconto  = 0 if desconto == "" else desconto
        _data_hora = datetime.datetime.now()
        _tipo = 2
        _funcionario_id = session['id']
        _lista_comandas = []
        for id_comanda in _id_comandas:
            _comanda = Comanda()
            _comanda.id_comanda = id_comanda
            _comanda.status_comanda = 1
            _comanda.status_pagamento = 1
            _lista_comandas.append(_comanda)
        
        
        _comanda_aux = Comanda()
        _mensagem, _id_recebimento = _comanda_aux.recebeFiados(_lista_comandas, _valor_final, _valor_total, _valor_desconto, _data_hora, _tipo, _funcionario_id)
        return jsonify(erro = False, mensagem = _mensagem, id_recebimento = _id_recebimento)
        
        

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_comanda.route("/comandasCliente")
@validaSessao
def comandasCliente():    
    _comanda = Comanda()
    _comanda.cliente_id = session['id']
    _comandas = _comanda.buscaComandasPorCliente()
    return render_template('formListaComandasCliente.html', comandas = _comandas)
    
@bp_comanda.route("/buscaComandaProdutosPorId", methods = ['POST'])
@validaSessao
def buscaComandaProdutosPorId():
    try:
        _comanda = Comanda()
        _comanda.id_comanda = request.form['id_comanda']
        _produtos = _comanda.selectProdutosPorIdComanda()

        return jsonify(erro = False, produtos = _produtos)
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)



@bp_comanda.route("/geraPDFRecebimento", methods = ['POST'])
@validaSessao
def geraPDFRecebimento():

    pdf = PDF()
    if request.form['tipo'] == 1:
        pdf.pdfRecebimentoAVista(request.form['id_recebimento'])
    else:
        pdf.pdfRecebimentoFiado(request.form['id_recebimento'])
    

    send_file('recebimento.pdf', attachment_filename='recebimento.pdf')

    os.startfile('recebimento.pdf')#abre o PDF

    return jsonify(erro = False)


