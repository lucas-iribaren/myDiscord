DELETE FROM categorie;

DELETE FROM channel;

DELETE FROM notification;

DELETE FROM message WHERE id_channel = 1;

DELETE FROM channel WHERE id = 1;

DELETE FROM message;