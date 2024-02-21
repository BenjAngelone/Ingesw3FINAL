import unittest
from flask import jsonify
from backend import app
import time
from backend import app, conectar_a_bd, contar_frecuencias
time.sleep(25)
class TestBackend(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_recibir_texto(self):
        # Mock de la solicitud de entrada
        response = self.app.post('/backend', json={'texto': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_contar_frecuencias(self):
        # Mock de la conexión a la base de datos
        mock_conexion_db = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('test', 2), ('example', 3)]
        mock_conexion_db.cursor.return_value = mock_cursor

        # La función conectar_a_bd se usa indirectamente dentro de contar_frecuencias
        frecuencias = contar_frecuencias(mock_conexion_db)

        self.assertEqual(len(frecuencias), 2)
        self.assertEqual(frecuencias[0]['palabra'], 'test')
        self.assertEqual(frecuencias[0]['frecuencia'], 2)
        self.assertEqual(frecuencias[1]['palabra'], 'example')
        self.assertEqual(frecuencias[1]['frecuencia'], 3)

    def test_test_backend(self):
        with app.test_client() as client:
            response = client.get('/test')
