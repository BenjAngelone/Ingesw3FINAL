import unittest

class TestBackend(unittest.TestCase):

    def test_endpoint_test(self):
        # Se envía una solicitud GET al endpoint de prueba
        response = app.test_client().get('/test')

        # Se verifica el código de respuesta
        self.assertEqual(response.status_code, 200)

        # Se verifica el contenido de la respuesta
        data = response.get_json()
        self.assertEqual(data['respuesta'], "Backend funcionando correctamente")

if __name__ == '__main__':
    unittest.main()
