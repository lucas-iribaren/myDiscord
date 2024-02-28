-- Active: 1708523909123@@127.0.0.1@3306@mydiscord
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
    WHEN id = 5 THEN 1
    WHEN id = 6 THEN 2
    WHEN id = 7 THEN 3
END;


-- Restart auto_incre (going at end if you have some data)--
ALTER TABLE channel AUTO_INCREMENT = 1; 
--------------------------------------------

UPDATE channel
SET id = CASE
    WHEN id = 4 THEN 1
    WHEN id = 5 THEN 2
    WHEN id = 6 THEN 3
    WHEN id = 7 THEN 4
    WHEN id = 8 THEN 5
    WHEN id = 9 THEN 6
    WHEN id = 10 THEN 7
    WHEN id = 11 THEN 8
    WHEN id = 12 THEN 9
    WHEN id = 13 THEN 10
END;



