import unittest
from flask import jsonify
from backend import app

class TestBackend(unittest.TestCase):
    def test_test_backend(self):
        with app.test_client() as client:
            response = client.get('/test')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data["respuesta"], "Ok")

if __name__ == '__main__':
    unittest.main()
