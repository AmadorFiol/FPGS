#flask --app $rutaArchivo run
from flask import Flask
#Transformamos el archivo en un projecto de flask
app = Flask(__name__)
#Indico la ruta web y llamo a las funciones seguidamente establecidas debajo
@app.route("/")
def hello_world():
    return "Hello, World!"