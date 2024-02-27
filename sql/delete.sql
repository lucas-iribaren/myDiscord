-- Active: 1708523909123@@127.0.0.1@3306@mydiscord
DELETE FROM categorie;

DELETE FROM channel;

DELETE FROM notification;

DELETE FROM message WHERE id_channel = 1;

DELETE FROM channel WHERE id = 1;

DELETE FROM message;