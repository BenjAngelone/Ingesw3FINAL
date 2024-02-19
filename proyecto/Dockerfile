# Usa una imagen base de Node.js
FROM node:14

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY package*.json ./
COPY public ./public
COPY src ./src

# Instala las dependencias
RUN npm install

# Construye la aplicación React
RUN npm run build

# Expone el puerto en el que se ejecutará la aplicación (puedes ajustar esto según tu aplicación React)
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["npm", "start"]
