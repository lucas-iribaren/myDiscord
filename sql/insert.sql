INSERT INTO role (name)
VALUES ('membre'),
('modérateur');

INSERT INTO user (pseudo, mail, password, id_role) 
VALUES 
    ('lucas', 'lucas.discord@laplateforme.io', 'discord', 1),
    ('kevin', 'kevin.discord@laplateforme.io', 'discord', 2),
    ('lucy', 'lucy.discord@laplateforme.io', 'discord', 1);

INSERT INTO categorie(name)
VALUES ("Général"),
("Need for speed"),
("League of Legend"),
("Minecraft");

INSERT INTO channel(nom,id_categorie)
VALUES ("règle",1),
("info",1),
("suggestion",1);