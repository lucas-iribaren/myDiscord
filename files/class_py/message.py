import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.accueil import Accueil
from datetime import datetime
accueil = Accueil()

class Message(Interface, Database):
    def __init__(self, user):         
        Database.__init__(self)
        Interface.__init__(self)
        self.user = user       
        self.curent_time = datetime.now() 
        self.input_texts_message = {'message':''}
        self.active_input = None  # Pour suivre le champ de texte actif      
        
    def add_message(self, input_text, user, heure, id_channel):
        sql = "INSERT INTO message(text,auteur,heure,id_channel) VALUES (%s,%s,%s,%s);"
        self.execute_sql(sql, (input_text, user, heure, id_channel))
        
    def message_display(self, x_message, y_message, largeur_message, hauteur_message, radius_message):
        self.solid_rect_radius(self.light_grey, x_message, y_message, largeur_message, hauteur_message, radius_message)
        self.text(15, accueil.user_data, self.black, x_message, y_message - 30)
        self.text(14, self.curent_time, self.white, x_message + 30, y_message - 30)
        self.text(13, self.input_texts_message['message'], self.white, x_message + 30, y_message + 30)        
    
    
        
        
