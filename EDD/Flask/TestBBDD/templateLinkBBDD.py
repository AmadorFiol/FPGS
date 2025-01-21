#flask --app $rutaArchivo run --debug
from flask import Flask,jsonify,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#-----Configuramos conexión a BBDD-----#
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///example.db'#Donde esta la BBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False #Desactivar logs
db=SQLAlchemy(app)

#-----Declaramos clases-----#
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)

#----Declaramos funciones/webs-----#
@app.route("/users")
def get_users():
    users=User.query.all #Select * From User
    #return jsonify([{"id":user.id,"name":user.name,"email":user.email} for user in users])
    return render_template("users.html",users=users)

@app.route("/add_user/<name>/<email>")
def add_user(name,email):
    new_user=User(name=name,email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"Usuario {name} agregado correctamente"
#-----Main-----#
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)