from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, resources={r"/backend": {"origins": "*"}})

def conectar_a_bd():
    conexion_db = mysql.connector.connect(
        host="mysql",
        user="root",
        password="Benjamin15",
        database="basededatospalabra"
    )
    return conexion_db

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
    if conexion_db is not None:
    print("¡Acceso a la base de datos confirmado!")
    # ... (resto del código dentro del bloque `if`)
else:
    print("Error al conectar a la base de datos")
    return jsonify({"error": "No se pudo conectar a la base de datos"})
    
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
# ...


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
