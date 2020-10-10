from flask import Blueprint, render_template

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
    return render_template('formFuncionario.html')