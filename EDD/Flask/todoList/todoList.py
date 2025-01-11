#flask --app $rutaArchivo run --debug
from flask import Flask,render_template,request
tareasArray=[]
app = Flask(__name__)
@app.route("/")
def tareas():  
    return render_template("/index.html",tareas=tareasArray)

@app.route("/add", methods=["POST","GET"])
def addTarea():
    if request.method=="POST":
        tareaUser=request.form["nombre"]
        tareasArray.append({"name":tareaUser,"is_completed":False})

    return render_template("/add.html",tareas=tareasArray)

@app.route("/remove", methods=["POST","GET"])
def removeTarea():
    if request.method=="POST":
        tareaUser=request.form["nombre"]
        for tarea in tareasArray:
            if tarea["name"]==tareaUser:
                tareasArray.remove(tarea)

    return render_template("/remove.html",tareas=tareasArray)

@app.route("/complete", methods=["POST","GET"])
def complete():
    if request.method=="POST":
        tareaUser=request.form["nombre"]
        for tarea in tareasArray:
            if tarea["name"]==tareaUser:
                tarea["is_completed"]=True

    return render_template("/complete.html",tareas=tareasArray)

if __name__ == "__app__":
    app.run(debug=True)