from flask import Flask

from mod_home.home import bp_home
from mod_cliente.cliente import bp_cliente
from mod_funcionario.funcionario import bp_funcionario

app = Flask(__name__)
app.register_blueprint(bp_home)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_funcionario)



if __name__ == "__main__":
    app.run()