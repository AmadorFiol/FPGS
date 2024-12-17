#flask --app $rutaArchivo run --debug
from flask import Flask,render_template,request
#Transformamos el archivo en un projecto de flask
app = Flask(__name__)
@app.route("/form", methods=['GET','POST'])

def form():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        return f"<h1>Gracias {username}</h1><p>Te contactaremos en {email}</p>"
    
    return render_template("form.html")

if __name__ == "__app__":
    app.run(debug=True)