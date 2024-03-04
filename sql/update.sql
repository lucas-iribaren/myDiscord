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
    WHEN id = 5 THEN 1
    WHEN id = 6 THEN 2
    WHEN id = 7 THEN 3
END;


-- Restart auto_incre (going at end if you have some data)--
ALTER TABLE channel AUTO_INCREMENT = 1; 
--------------------------------------------

UPDATE channel
SET id = CASE
    WHEN id = 63 THEN 1
    WHEN id = 64 THEN 2
    WHEN id = 65 THEN 3
    WHEN id = 66 THEN 4
    WHEN id = 67 THEN 5
    WHEN id = 68 THEN 6
    WHEN id = 69 THEN 7
    WHEN id = 70 THEN 8
    WHEN id = 71 THEN 9
    WHEN id = 72 THEN 10
END;

UPDATE message
SET id = CASE
    WHEN id = 30 THEN 1
    WHEN id = 31 THEN 2
    WHEN id = 32 THEN 3
    WHEN id = 33 THEN 4
    WHEN id = 34 THEN 5
    WHEN id = 35 THEN 6
END;



