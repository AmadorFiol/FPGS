from flask import Flask, jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message":"Hola"})

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return jsonify({"saludo":f"Hola, {nombre}"})

if __name__=="__main__":
    app.run(debug=True)