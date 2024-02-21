import unittest
from flask import jsonify
from backend import app

class TestBackend(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        
    def tearDown(self):
        pass
        
    def test_test_backend(self):
        with app.test_client() as client:
            response = client.post('/test', json={"texto": "hello"})
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data["palabra_original"], "hello")
            self.assertEqual(data["palabra_en_espejo"], "olleh")

if __name__ == '__main__':
    unittest.main()
