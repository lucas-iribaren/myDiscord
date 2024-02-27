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
    WHEN id = 11 THEN 1
    WHEN id = 12 THEN 2
    WHEN id = 13 THEN 3
    WHEN id = 14 THEN 4
END;

UPDATE channel
SET id = CASE
    WHEN id = 11 THEN 1
    WHEN id = 12 THEN 2
    WHEN id = 13 THEN 3
    WHEN id = 14 THEN 3
END;