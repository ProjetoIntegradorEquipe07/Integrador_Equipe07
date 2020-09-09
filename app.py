from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Home da aplicação"

if __name__ == "__main__":
    app.run()