-- Active: 1707491285105@@127.0.0.1@3306@mydiscord
INSERT INTO role (name)
VALUES ('membre'),
('modérateur');

INSERT INTO user (pseudo, mail, password, id_role) 
VALUES 
    ('lucas', 'lucas.discord@laplateforme.io', 'discord', 1),
    ('kevin', 'kevin.discord@laplateforme.io', 'discord', 2),
    ('lucy', 'lucy.discord@laplateforme.io', 'discord', 1);

INSERT INTO categorie(name)
VALUES ("Bienvenue"),
("Minecraft"),
("League of Legends");


INSERT INTO channel (nom, status, communication, id_categorie)
VALUES ("Règlement",0,0,1),
("Informations",0,0,1),
("Discussion",0,0,2),
("Chat privé",0,1,2),
("Vocal",1,0,2),
("Vocal privé",1,1,2),
("Général",0,0,3),
("Chat privé",0,1,3),
("Vocal",1,0,3),
("Vocal privé",1,1,3);

