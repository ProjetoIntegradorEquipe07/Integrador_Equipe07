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

@bp_empresa.route("/salvaConfiguracoes", methods = ['POST'])
@validaSessao
@validaGrupo
def salvaConfiguracoes():
    try:
        _empresa = Empresa()
        _empresa.multa_atraso = request.form['multa_atraso']
        _empresa.taxa_juro_diario = request.form['taxa_juro_diario']

        _mensagem = _empresa.update()

        return jsonify(erro = False, mensagem = _mensagem)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
