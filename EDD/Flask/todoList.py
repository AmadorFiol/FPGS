#flask --app $rutaArchivo run
from flask import Flask
#Transformamos el archivo en un projecto de flask
app = Flask(__name__)
@app.route("/")

def mostrarLista():
    todoArray=["Hola","Adios"]
    for todo in todoArray:
        enviar="<p>",todo,"</p>"
        print(enviar)