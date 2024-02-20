import time
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/backend": {"origins": "*"}})

def conectar_a_bd():
    while True:
        try:
            conexion_db = mysql.connector.connect(
                host="mysql",
                user="root",
                password="Benjamin15",
                database="basededatospalabra"
            )
            print("Conexión exitosa a la base de datos")
            return conexion_db
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)
            print("Reintentando en 5 segundos...")
            time.sleep(5)  # Esperar 5 segundos antes de volver a intentar la conexión

@app.route('/test', methods=['GET'])
def test_backend():
    return jsonify({"respuesta": "Ok"})

# Resto de tu código...

if __name__ == '__main__':
    conexion_db = conectar_a_bd()  # Inicializar la conexión a la base de datos
    app.run(host='0.0.0.0', port=5000)
