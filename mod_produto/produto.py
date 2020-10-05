from flask import Blueprint, render_template

from mod_login.login import validaSessao

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/")
@validaSessao
def formListaProdutos():
    return render_template('formListaProdutos.html')

@bp_produto.route("formProduto")
@validaSessao
def formProduto():
    return render_template('formProduto.html')