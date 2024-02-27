-- Active: 1708523909123@@127.0.0.1@3306@mydiscord
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
("League of Legend");


INSERT INTO channel (nom, status, communication, id_categorie)
VALUES ("règle",0,0,1),
("info",0,0,1),
("général",0,0,2),
("chat privé",0,1,2),
("Vocal",1,0,2),
("Vocal privé",1,1,2),
("général",0,0,3),
("chat privé",0,1,3),
("Vocal",1,0,3),
("Vocal privé",1,1,3);

