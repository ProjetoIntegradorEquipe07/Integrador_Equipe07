from flask import Blueprint, render_template, request, url_for, jsonify

from mod_login.login import validaSessao

bp_comanda = Blueprint('comanda', __name__, url_prefix='/comanda', template_folder='templates')

@bp_comanda.route("/")
@validaSessao
def dashboard():
    return render_template('dashboard.html')

@bp_comanda.route("/addComanda", methods=['POST'])
@validaSessao
def addComanda():
    return render_template('formComanda.html')