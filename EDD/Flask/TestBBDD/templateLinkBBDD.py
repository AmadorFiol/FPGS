#flask --app $rutaArchivo run --debug
from flask import Flask,jsonify,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#-----Configuramos conexión a BBDD-----#
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///example.db'#Donde esta la BBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False #Desactivar logs
db=SQLAlchemy(app)

#-----Declaramos clases-----#
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), unique=True, nullable=False)

#----Declaramos funciones/webs-----#
@app.route("/users")
def get_users():
    usersArray=User.query.all #Select * From User
    #return jsonify([{"id":user.id,"name":user.name,"email":user.email} for user in users])
    return render_template("/users.html",usersArray=usersArray)

@app.route("/user/add/<name>/<email>")
def add_user(name,email):
    new_user=User(name=name,email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"Usuario {name} agregado correctamente"

@app.route("/user/<int:user_id>")
def get_user_id(user_id):
    user=User.query.get(user_id)
    if user:
        return jsonify({"id":user.id,"name":user.name,"email":user.email})
    else:
        return jsonify({"error":"Usuario no encontrado"}),404

@app.route("/user/delete/<int:user_id>",methods=["POST"])
def delete_user(user_id):
    user=User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":f"Usuario con id {user.id} eliminado correctamente"})
    else:
        return jsonify({"error":"Usuario no encontrado"}), 404
 
@app.route("/user/edit/<int:user_id>",methods=['POST'])
def edit_user(user_id):
    user=User.query.get(user_id)
    if not user:
        return jsonify({"error":"Usuario no encontrado"}), 404
    if request.method=="POST":
        user.name=request.form.get("name")
        user.email=request.form.get("email")
        db.session.commit()
        return redirect(url_for("users"))

#-----Main-----#
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)