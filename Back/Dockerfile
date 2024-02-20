# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY backend.py .

# Instala las dependencias
RUN pip install flask
RUN pip install flask-cors
RUN pip install mysql-connector-python
RUN apt-get update && apt-get install -y default-mysql-client

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "backend.py"]
