from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from functools import wraps

from mod_funcionario.funcionarioBD import Funcionario
from funcoes import Funcoes, LOG

bp_login = Blueprint('login', __name__, url_prefix="/", template_folder='templates')

# valida se o usuário esta ativo na sessão
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            #descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login', falhaSessao=1))
        else:
            #retorna os dados copiados da função original
            return f(*args, **kwargs)

    #retorna o resultado do if acima
    return decorated_function

def validaGrupo(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['grupo'] != 1:
            return redirect(url_for('home.home'))
        else:
            return f(*args, **kwargs)

    return decorated_function

@bp_login.route("/")
def login():
    return render_template('formLogin.html')

@bp_login.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login.login'))

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    _nome = request.form['usuario']
    _senha = Funcoes.criptografaSenha(request.form['senha'])
    

    funcionario = Funcionario()

    funcionario.nome = _nome
    funcionario.senha = _senha

    
    try:

        if funcionario.selectLogin():
            
            session.clear()
            session['usuario'] = funcionario.nome
            session['grupo'] = funcionario.grupo
            session['id'] = funcionario.id_funcionario

            Funcoes.criaLOG('Login feito com sucesso!', LOG.info)

            return jsonify(erro = False, nome = funcionario.nome)

        else:
            session['id'] = 0
            Funcoes.criaLOG('Usuario ou senha incorretos', LOG.warning)
            session.clear()
            return jsonify(erro = True)
    except Exception as e:
        session.clear()
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
            Funcoes.criaLOG(_mensagem_exception, LOG.error)
        else:
            _mensagem = 'Erro'
            _mensagem_exception = str(e)
            Funcoes.criaLOG(_mensagem_exception, 'error')
        return jsonify(erro_ex = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
