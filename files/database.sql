-- Active: 1707491285105@@127.0.0.1@3306@mydiscord
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

INSERT INTO channel(nom,id_categorie)
VALUES ("général",1);

CREATE TABLE user( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    pseudo VARCHAR(25),
    email VARCHAR(255) UNIQUE CHECK (REGEXP_LIKE(email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')),
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

INSERT INTO role (name)
VALUES ('membre'),
('modérateur');

INSERT INTO categorie(name)
VALUES ('public'),
("privé");

INSERT INTO user (pseudo, mail, password, id_role) 
VALUES ('lucas', 'lucas.discord@laplateforme.io', 'discord', 1);

INSERT INTO user (pseudo, mail, password, id_role) 
VALUES ('kevin', 'kevin.discord@laplateforme.io', 'discord', 2);

INSERT INTO user (pseudo, mail, password, id_role)
VALUES ('lucy', 'lucy.discord@laplateforme.io', 'discord', 1);







-- INSERT INTO message (text, auteur)
-- VALUES ('Contenu du message', 'Auteur du message');
