FROM mysql:latest

# Variables de entorno para configurar la base de datos
ENV MYSQL_ROOT_PASSWORD=Benjamin15
ENV MYSQL_DATABASE=basededatospalabra

# Copiar el script SQL a la carpeta /docker-entrypoint-initdb.d/
COPY DATABASE.sql /docker-entrypoint-initdb.d/
