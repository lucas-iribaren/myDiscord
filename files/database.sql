-- Active: 1706528093603@@127.0.0.1@3306@mydiscord
CREATE DATABASE myDiscord;

USE myDiscord;

CREATE TABLE role(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200)
);

CREATE TABLE categorie(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25)
);
CREATE TABLE notification(
    id INT PRIMARY KEY AUTO_INCREMENT,
    text TEXT,
    auteur VARCHAR(255),
    heure DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE channel(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(30),
    id_categorie INT
);

CREATE TABLE user( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    pseudo VARCHAR(25),
    mail VARCHAR(200) UNIQUE,
    password VARCHAR(200),
    id_role INT,
    FOREIGN KEY (id_role) REFERENCES role(id)
);

CREATE TABLE message(
    id INT PRIMARY KEY AUTO_INCREMENT,
    text TEXT,
    auteur VARCHAR(255),
    heure DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_channel INT,
    FOREIGN KEY (id_channel) REFERENCES channel(id)
);





-- INSERT INTO message (text, auteur)
-- VALUES ('Contenu du message', 'Auteur du message');
