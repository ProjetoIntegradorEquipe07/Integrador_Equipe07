from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

from mod_funcionario.funcionarioBD import Funcionario
from funcoes import Funcoes

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

@bp_login.route("/")
def login():
    return render_template('formLogin.html')

@bp_login.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login.login'))

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    _cpf = request.form['cpf']
    _senha = Funcoes.criptografaSenha(request.form['senha'])
    

    funcionario = Funcionario()

    funcionario.cpf = _cpf
    funcionario.senha = _senha

    

    if funcionario.selectLogin():
        
        session.clear()
        session['usuario'] = funcionario.nome
        session['grupo'] = funcionario.grupo
        return redirect(url_for('home.home'))

    else:
        return redirect(url_for('login.login', falhaLogin=1))