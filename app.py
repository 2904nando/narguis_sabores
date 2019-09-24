from sincronizarBD import categorias, essencias, misturas
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", essencias=essencias)

@app.route('/misturas')
def misturas():
    return render_template("misturas.html", misturas=misturas)

if __name__ == "__main__":
    app.run(debug=True)