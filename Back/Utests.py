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

        self.assertEqual(len(frecuencias), 4)
        self.assertEqual(frecuencias[0]['palabra'], 'test')
        self.assertEqual(frecuencias[0]['frecuencia'], 2)
        self.assertEqual(frecuencias[1]['palabra'], 'example')
        self.assertEqual(frecuencias[1]['frecuencia'], 3)
    def test_test_backend(self):
        with app.test_client() as client:
            # Enviamos una solicitud GET a '/test' con la palabra 'hello'
            response = client.get('/test')
            data = response.get_json()
    
            # Verificamos que la solicitud fue exitosa
            self.assertEqual(response.status_code, 200)
    
            # Verificamos que la palabra invertida sea la correcta
            self.assertEqual(data['palabra_original'], 'hello')
            self.assertEqual(data['palabra_en_espejo'], 'olleh')
    
            # Imprimimos un mensaje indicando que la prueba pasó exitosamente
            print("Prueba test_test_backend pasó exitosamente.")
    def test_test_backend(self):
        with app.test_client() as client:
            response = client.get('/test')
