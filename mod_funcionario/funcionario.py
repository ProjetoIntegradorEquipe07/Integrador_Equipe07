from flask import Blueprint, render_template

from mod_login.login import validaSessao

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder="templates")

@bp_funcionario.route("/")
@validaSessao
def formListaFuncionarios():
    return render_template('formListaFuncionarios.html')

@bp_funcionario.route("/formFuncionario")
@validaSessao
def formFuncionario():
    return render_template('formFuncionario.html')