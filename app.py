from sincronizarBD import categorias, essencias, misturas
from flask import Flask, render_template, redirect, url_for, request
import db_actions

import criadorEssencia

app = Flask(__name__)

@app.route('/')
def index():
    essencias = db_actions.getAllEssenciasSimple()
    return render_template("index.html", essencias=essencias)

@app.route('/misturas')
def misturas():
    misturas = db_actions.getAllMisturasSimple()
    return render_template("misturas.html", misturas=misturas)

@app.route('/form_criar_essencias')
def form_criar_essencias():
    return render_template("criador_essencias.html")

@app.route('/criar_essencia', methods=['POST'])
def criar_essencia():
    criadorEssencia.criarEssencia(request.form['nome'],
                                  request.form['marca'],
                                  request.form['desc'],
                                  request.form['preco'],
                                  request.form['foto'],
                                  request.form['qtd'],
                                  request.form['categoria'])
    return redirect(url_for("index"))

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == "__main__":
    app.run(debug=True)