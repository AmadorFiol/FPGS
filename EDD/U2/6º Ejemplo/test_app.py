import unittest

from app import app, db, User


class MyTestCase(unittest.TestCase):

    # Definimos el setup que se ejecuta antes de cada test
    def setUp(self):
        # Definimos la configuracion de testing
        app.config['TESTING'] = True
        # Definimos el tipo de base de datos (sqlite) y el fichero será en memoria
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        # Definimos un cliente para simular al navegador
        self.client = app.test_client()

        # Creamos la Base de datos
        with app.app_context():
            db.create_all()

    # Se ejecutará despues de cada test
    # Borrando la BBDD
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Test de creado OK
    # Debemos comprobar que el servidor devuelve el http correcto (201)
    # Debemos comprobar que devuelve el contenido correcto (juan)
    def test_create_user(self):
        # Llamamos al endpoint con POST y le pasamos el JSON con el contenido a añadir
        response = self.client.post("/users", json={"name": "juan"})
        # Comprobamos que devuelve 201
        self.assertEqual(response.status_code, 201)

        # Recuperamos el contenido JSON que devuelve el endpoint
        data = response.get_json()
        # Buscamos el campo 'name', que es "juan"
        self.assertEqual(data['name'], "juan")

    # Test de creado NOK
    def test_create_user_error(self):
        # Dara error porque no es 'name', es 'telefono'
        response = self.client.post("/users", json={"telefono": "juan"})
        # Comprobamos que devuelve 400
        self.assertEqual(response.status_code, 400)

    # Test de getAll OK
    def test_get_users(self):
        # Añadimos el contenido a la BBDD directamente, no necesitamos los ID
        with app.app_context():
            db.session.add(User(name="Pepe"))
            db.session.add(User(name="Jose"))
            db.session.commit()

        # Comprobamos que devuelve 200
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)

        # Comprobamos que el contenido es correcto
        data = response.get_json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Pepe")
        self.assertEqual(data[1]['name'], "Jose")

    # Test de getUserById OK
    def test_get_user_by_id(self):
        # Creamos un usuario primero porque necesitamos su ID
        response = self.client.post("/users", json={"name": "juan"})
        # Recuperamos el ID
        user_id = response.get_json()['id']

        # Llamamos al endpoint que queremos probar usando el ID anterior
        response2 = self.client.get(f"/user/{user_id}")
        # Comprobamos que devuelve 200
        self.assertEqual(response2.status_code, 200)
        # Y efectivamente, vemos que es Juan
        data = response2.get_json()
        self.assertEqual(data['name'], "juan")

    # Test de getUserById NOK
    def test_get_user_by_id_error(self):
        # Buscamos un id inventado que dará error
        response2 = self.client.get("/user/999")
        # Comprobamos que devuelve 404
        self.assertEqual(response2.status_code, 404)

        # Comprobamos que el contenido que devuelve contiene nuestro mensaje de error
        data = response2.get_json()
        self.assertEqual(data['error'], "Usuario no encontrado")


if __name__ == '__main__':
    unittest.main()
