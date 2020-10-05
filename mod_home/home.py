from flask import Blueprint, render_template

from mod_login.login import validaSessao

bp_home = Blueprint('home', __name__, url_prefix='/home', template_folder='templates')

@bp_home.route("/")
@validaSessao
def home():
    return render_template("home.html")