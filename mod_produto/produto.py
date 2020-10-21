from flask import Blueprint, render_template, request, jsonify

from mod_login.login import validaSessao
from mod_produto.produtoBD import Produto

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/")
@validaSessao
def formListaProdutos():
    _produto = Produto()
    lista_produto = _produto.selectAll()

    return render_template('formListaProdutos.html', lista_produto = lista_produto)

@bp_produto.route("formProduto")
@validaSessao
def formProduto():
    _produto = Produto()

    return render_template('formProduto.html', produto = _produto)

@bp_produto.route("/addProduto", methods=['POST'])
@validaSessao
def addProduto():
    try:
        _nome = request.form['nome']
        _descricao = request.form['descricao']
        _valor_unitario = request.form['valor_unitario']

        _produto = Produto(0, _nome, _descricao, "", _valor_unitario)

        _mensagem = _produto.insert()

        return jsonify(erro = False, mensagem = _mensagem)
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)