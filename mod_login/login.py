from flask import Blueprint, render_template, request, redirect, url_for

bp_login = Blueprint('login', __name__, url_prefix="/", template_folder='templates')

@bp_login.route("/")
def login():
    return render_template('formLogin.html')

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    _nome = request.form['usuario']
    _senha = request.form['senha']

    if _nome == 'admin' and _senha == 'admin':
        return redirect(url_for('home.home'))

    else:
        return redirect(url_for('login.login', falhaLogin=1))