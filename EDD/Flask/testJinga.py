#flask --app $rutaArchivo run
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title="Test de Jinja"
    desc="Ahora esto es otra desc"
    return render_template("index.html",title=title,desc=desc)

@app.route("/users")
def users():
    usersArray=[
        {"name":"Alice","age":30,"is_admin":True},
        {"name":"Bob","age":24,"is_admin":False},
        {"name":"Charlie","age":35,"is_admin":True}
    ]
    return render_template("users.html",usersArray=usersArray)

if __name__ == "__app__":
    app.run(debug=True)