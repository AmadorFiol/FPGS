import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.testing=True
        self.client=app.test_client()
    
    def test_home(self):
        response=self.client.get("/")
        
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{"message":"Hola"})

    def test_saludo(self):
        response=self.client.get("/saludo/amador")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{"saludo":"Hola, amador"})
        

if __name__ == '__main__':
    unittest.main()