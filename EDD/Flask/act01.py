# flask --app $rutaArchivo run
from flask import Flask

# Transformamos el archivo en un projecto de flask
app = Flask(__name__)


@app.route("/")
def main():
    return ("<h1>Las opciones son las siguientes</h1>"
            "<a href=http://127.0.0.1:5000/jose>'Ejemplo titulo'</a><p></p>"
            "<a href=http://127.0.0.1:5000/pepe>'Ejemplo boton'</a><p></p>"
            "<a href=http://127.0.0.1:5000/alejandro>'Ejemplo link'</a><p></p>"
            "<a href=http://127.0.0.1:5000/lluis>'Ejemplo imagen'</a>")


@app.route("/jose")
def jose():
    return "<h1>Ejemplo Titulo</h1>"


@app.route("/pepe")
def pepe():
    return "<button>Ejemplo Boton</button>"


@app.route("/alejandro")
def alenjadro():
    return "<a href=https://media1.tenor.com/m/AqyLIJ48wQMAAAAd/pedro-racoon.gif> Pedro Pedro Pedro</a>"


@app.route("/lluis")
def lluis():
    return "<img border='0' src='https://wallpapers-clan.com/wp-content/uploads/2023/11/chibi-hatsune-miku-minimalist-desktop-wallpaper-preview.jpg' height=500 width=500>"
