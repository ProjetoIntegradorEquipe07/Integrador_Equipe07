from flask import Blueprint, render_template, request, jsonify

from mod_login.login import validaSessao
from mod_funcionario.funcionarioBD import Funcionario

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder="templates")

@bp_funcionario.route("/")
@validaSessao
def formListaFuncionarios():
    funcionario = Funcionario()
    _funcionarios = funcionario.selectAll()
    return render_template('formListaFuncionarios.html', funcionarios = _funcionarios)

@bp_funcionario.route("/formFuncionario")
@validaSessao
def formFuncionario():
    _funcionario = Funcionario()
    return render_template('formFuncionario.html', funcionario = _funcionario)

@bp_funcionario.route("/addFuncionario",methods=['POST'])
@validaSessao
def addFuncionario():
    _mensagem = ""    
    try:
        _nome = request.form['nome']
        _cpf = request.form['cpf']
        _telefone = request.form['telefone']
        _senha = request.form['senha']
        _matricula = request.form['matricula']
        _grupo = request.form['grupo']

        funcionario = Funcionario(0, _nome, _cpf, _telefone, _senha, _matricula, _grupo)


        _mensagem = funcionario.insert()
        return jsonify(erro = False, mensagem = _mensagem)
    except Exception as e:
        _mensagem_erro, _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem_erro, mensagem_exception = _mensagem_exception)

@bp_funcionario.route('/formEditFuncionario', methods=['POST'])
@validaSessao
def formEditFuncionario():
    _funcionario = Funcionario()
    _funcionario.id_funcionario = request.form['id_funcionario']
    _funcionario.selectOne()

    return render_template('formFuncionario.html', funcionario = _funcionario)

@bp_funcionario.route("/editFuncionario",methods=['POST'])
@validaSessao
def editFuncionario():
    _mensagem = ""    
    try:
        _id_funcionario = request.form['id_funcionario']
        _nome = request.form['nome']
        _cpf = request.form['cpf']
        _telefone = request.form['telefone']
        _senha = request.form['senha']
        _matricula = request.form['matricula']
        _grupo = request.form['grupo']

        funcionario = Funcionario(_id_funcionario, _nome, _cpf, _telefone, _senha, _matricula, _grupo)


        _mensagem = funcionario.update()
        return jsonify(erro = False, mensagem = _mensagem)
    except Exception as e:
        _mensagem_erro, _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem_erro, mensagem_exception = _mensagem_exception)

@bp_funcionario.route("/deleteFuncionario", methods = ['POST'])
@validaSessao
def deleteFuncionario():
    _mensagem = ""
    try:        
        _funcionario = Funcionario()
        _funcionario.id_funcionario = request.form['id_funcionario']
        _mensagem = _funcionario.delete()

        return jsonify(erro = False, mensagem = _mensagem)

    except Exception as e:
        _mensagem_erro, _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem_erro, mensagem_exception = _mensagem_exception)