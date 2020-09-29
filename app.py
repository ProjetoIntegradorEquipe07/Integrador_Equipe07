from flask import Flask, render_template

from mod_home.home import bp_home

app = Flask(__name__)
app.register_blueprint(bp_home)



if __name__ == "__main__":
    app.run()