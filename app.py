from flask import Flask, render_template

from mod_home.home import bp_home
from mod_cliente.cliente import bp_cliente

app = Flask(__name__)
app.register_blueprint(bp_home)
app.register_blueprint(bp_cliente)



if __name__ == "__main__":
    app.run()