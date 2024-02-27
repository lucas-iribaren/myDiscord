-- Active: 1707491285105@@127.0.0.1@3306@mydiscord
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

UPDATE categorie
SET id = CASE
    WHEN id = 15 THEN 1
    WHEN id = 16 THEN 2
    WHEN id = 17 THEN 3
END;


UPDATE channel
SET id = CASE
    WHEN id = 53 THEN 1
    WHEN id = 54 THEN 2
    WHEN id = 55 THEN 3
    WHEN id = 56 THEN 4
    WHEN id = 57 THEN 5
    WHEN id = 58 THEN 6
    WHEN id = 59 THEN 7
    WHEN id = 60 THEN 8
    WHEN id = 61 THEN 9
    WHEN id = 62 THEN 10
END;



