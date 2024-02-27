-- Active: 1708523909123@@127.0.0.1@3306@mydiscord
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









