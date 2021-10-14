from src.classes.filme import Filme
from src.classes.serie import Serie
from src.dao.serie_dao import SerieDAO
from src.bd.bd_connection import bd
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/series', methods=['GET']) 
def series():
    return jsonify(bd.open_in_read_mode())

@app.route('/filmes', methods=['GET']) 
def filmes():
    nova_serie = Serie(1, "Breaking Bad", "Ação", "Inglês", "Espanhol", 2011, 53)

    return f'''
    <html>
        <h1>FILMES</h1>

        Nome: <input type="Text" ></input> <br>
        Genero: <input type="Text" ></input> <br>
        Idioma: <input type="Text" ></input> <br>
        Legenda: <input type="Text" ></input> <br>
        Ano: <input type="Text" ></input> <br>
        Duração: <input type="Text" ></input> <br>
        
        <input type="submit" value="Salvar"></input>


        <table class=" aligncenter" style="height: 89px;" border="1" width="195">
            <tbody>
                <tr>
                    <th style="text-align: left;">Nome</th>
                    <th style="text-align: left;">Genero</th>
                    <th style="text-align: left;">Idioma</th>
                    <th style="text-align: left;">Legenda</th>
                    <th style="text-align: left;">Ano</th>
                    <th style="text-align: left;">Duração</th>
                </tr>
                <tr>
                    <td>{nova_serie.nome}</td>
                    <td>{nova_serie.genero}</td>
                    <td>{nova_serie.idioma}</td>
                    <td>{nova_serie.legenda}</td>
                    <td>{nova_serie.ano}</td>
                    <td>{nova_serie.duracao}</td>
                </tr>
                <tr>
                    <td>{nova_serie.nome}</td>
                    <td>{nova_serie.genero}</td>
                    <td>{nova_serie.idioma}</td>
                    <td>{nova_serie.legenda}</td>
                    <td>{nova_serie.ano}</td>
                    <td>{nova_serie.duracao}</td>
                </tr>
                <tr>
                    <td>{nova_serie.nome}</td>
                    <td>{nova_serie.genero}</td>
                    <td>{nova_serie.idioma}</td>
                    <td>{nova_serie.legenda}</td>
                    <td>{nova_serie.ano}</td>
                    <td>{nova_serie.duracao}</td>
                </tr>
            </tbody>
        </table>

    </html>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')