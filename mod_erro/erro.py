from flask import Blueprint, render_template

from mod_login.login import validaSessao

bp_erro = Blueprint('erro', __name__, url_prefix='/', template_folder='templates')

@bp_erro.app_errorhandler(404)
@validaSessao
def erro404(error):
    return render_template('form_erro_404.html')

@bp_erro.app_errorhandler(500)
@validaSessao
def erro500(error):
    return render_template('form_erro_500.html')