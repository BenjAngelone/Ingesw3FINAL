import time
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

print("Retraso en 15 segundos...")
time.sleep(15)

app = Flask(__name__)
CORS(app, resources={r"/backend": {"origins": "*"}})

def conectar_a_bd():
    while True:
        try:
            conexion_db = mysql.connector.connect(
                host="basededatos:3306",
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
    if request.method == 'POST':
        print("Recibiendo solicitud...")
        datos = request.get_json()
        palabra_original = datos.get('texto')
        palabra_en_espejo = palabra_original[::-1]

        print('Texto recibido en el backend:', palabra_original)
        print('Palabra en espejo:', palabra_en_espejo)

        return jsonify({"palabra_original": palabra_original, "palabra_en_espejo": palabra_en_espejo})
    else:
        return jsonify({"mensaje": "Método no permitido"}), 405

@app.route('/backend', methods=['POST'])
def recibir_texto():
    print("Recibiendo solicitud...")
    datos = request.get_json()
    palabra_original = datos.get('texto')
    palabra_en_espejo = palabra_original[::-1]

    print('Texto recibido en el backend:', palabra_original)
    print('Palabra en espejo:', palabra_en_espejo)

    # Comprobar el acceso a la base de datos
    conexion_db = conectar_a_bd()
    cursor = conexion_db.cursor() 
    sql = "SELECT 1"
    cursor.execute(sql)

    # Leer y descartar los resultados de la consulta
    cursor.fetchall()

    if cursor.rowcount == 1:
        print("Acceso a la base de datos confirmado")
    else:
        print("Error al acceder a la base de datos")

    cursor.close()  # Cerrar el cursor después de usarlo

    # Guardar datos en la base de datos
    cursor = conexion_db.cursor()
    sql = "INSERT INTO palabras (original, en_espejo) VALUES (%s, %s)"
    valores = (palabra_original, palabra_en_espejo)
    cursor.execute(sql, valores)
    conexion_db.commit()

    # Contar la frecuencia de cada palabra
    frecuencias = contar_frecuencias(conexion_db)

    return jsonify({'palabra_en_espejo': palabra_en_espejo, 'frecuencias': frecuencias})

def contar_frecuencias(conexion_db):
    cursor = conexion_db.cursor()
    sql = "SELECT original, COUNT(*) AS frecuencia FROM palabras GROUP BY original ORDER BY frecuencia DESC"
    cursor.execute(sql)
    resultados = cursor.fetchall()

    frecuencias = [{'palabra': palabra, 'frecuencia': frecuencia} for palabra, frecuencia in resultados]
    print('Frecuencias:', frecuencias)

    cursor.close()  # Cerrar el cursor después de usarlo

    return frecuencias

if __name__ == '__main__':
    conexion_db = conectar_a_bd()  # Inicializar la conexión a la base de datos
    app.run(host='0.0.0.0', port=5000)
