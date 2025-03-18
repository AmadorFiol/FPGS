from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({"error": "Nombre es requerido"}), 400

    usuario = User(name=data['name'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"id": usuario.id, "name": usuario.name}), 201


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])


@app.route("/user/<int:user_id>")
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"id": user.id, "name": user.name})

if __name__ == '__main__':
    app.run(debug=True)
