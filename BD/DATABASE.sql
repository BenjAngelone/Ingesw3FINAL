CREATE DATABASE IF NOT EXISTS basededatospalabra;
USE basededatospalabra;

CREATE TABLE IF NOT EXISTS palabras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original VARCHAR(255) NOT NULL,
    en_espejo VARCHAR(255) NOT NULL
);
