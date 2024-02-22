-- Active: 1707490841602@@127.0.0.1@3306
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

INSERT INTO role (name)
VALUES ('membre'),
('modérateur');

INSERT INTO user (pseudo, mail, password, id_role) 
VALUES 
    ('lucas', 'lucas.discord@laplateforme.io', 'discord', 1),
    ('kevin', 'kevin.discord@laplateforme.io', 'discord', 2),
    ('lucy', 'lucy.discord@laplateforme.io', 'discord', 1);


DELETE FROM notification;

# A FAIRE DANS L'ORDER

DELETE FROM message WHERE id_channel = 1;

DELETE FROM channel WHERE id = 1;

ALTER TABLE channel
MODIFY COLUMN nom VARCHAR(50),
ADD COLUMN status TINYINT(1),
ADD COLUMN communication TINYINT(1),
MODIFY COLUMN id_categorie INT,
ADD CONSTRAINT fk_categorie FOREIGN KEY (id_categorie) REFERENCES categorie(id);

ALTER TABLE channel
MODIFY COLUMN status TINYINT(1) AFTER nom,
MODIFY COLUMN communication TINYINT(1) AFTER status,
MODIFY COLUMN id_categorie INT AFTER communication;

DELETE FROM categorie;

DELETE FROM channel;

INSERT INTO categorie(name)
VALUES ("Général"),
("Need for speed"),
("League of Legend"),
("Minecraft");

UPDATE categorie
SET id = CASE
    WHEN id = 8 THEN 1
    WHEN id = 9 THEN 2
    WHEN id = 10 THEN 3
    WHEN id = 11 THEN 4
END;

INSERT INTO channel(nom,id_categorie)
VALUES ("règle",1),
("info",1),
("suggestion",1);

UPDATE channel
SET id = CASE
    WHEN id = 20 THEN 1
    WHEN id = 21 THEN 2
    WHEN id = 22 THEN 3
END;
















-- INSERT INTO message (text, auteur)
-- VALUES ('Contenu du message', 'Auteur du message');
