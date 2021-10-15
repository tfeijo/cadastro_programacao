from src.classes.filme import Filme
from src.classes.serie import Serie
from src.dao.serie_dao import SerieDAO
from src.bd.bd_connection import bd
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
@app.route('/series', methods=['GET']) 
def series():
    return jsonify(bd.open_in_read_mode())

@app.route('/filmes', methods=['GET']) 
def filmes():
    nova_serie = Serie(1, "Breaking Bad", "Ação", "Inglês", "Espanhol", 2011, 53)
    variavel = "Raian"
    return render_template('filmes.html', variavel = variavel)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')