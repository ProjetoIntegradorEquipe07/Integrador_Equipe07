from flask import Blueprint, render_template, jsonify, request

from mod_empresa.empresaDB import Empresa
from mod_login.login import validaSessao, validaGrupo

bp_empresa = Blueprint('empresa', __name__, url_prefix='/empresa', template_folder='templates')

@bp_empresa.route("/")
@validaSessao
@validaGrupo
def configuracoes():
    _empresa = Empresa()
    _configuracoes = _empresa.select()
    return render_template('configuracoes.html', configuracoes = _configuracoes)