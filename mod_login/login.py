from flask import Blueprint, render_template, request, redirect, url_for

bp_login = Blueprint('login', __name__, url_prefix="/", template_folder='templates')

@bp_login.route("/")
def login():
    return render_template('formLogin.html')

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    pass