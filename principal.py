from src.classes.filme import Filme
from src.classes.serie import Serie
from src.dao.serie_dao import SerieDAO
from src.bd.bd_connection import bd
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route('/', methods=['GET']) 
def home():
    return '''<html>'
        <center>Eu estou online! - Hello World<center/>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')