from flask import Blueprint, render_template

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder="templates")

@bp_funcionario.route("/")
def formListaFuncionarios():
    return render_template('formListaFuncionarios.html')

@bp_funcionario.route("/formFuncionario")
def formFuncionario():
    return render_template('formFuncionario.html')