from flask import Blueprint, render_template

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/")
def formListaProdutos():
    return render_template('formListaProdutos.html')

@bp_produto.route("formProduto")
def formProduto():
    return render_template('formProduto.html')