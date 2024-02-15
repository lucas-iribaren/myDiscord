import pygame
from datetime import datetime
from files.class_py.interface import Interface
from files.class_py.database import Database

class Message(Database, Interface):
    def __init__(self, user):         
        Database.__init__(self)
        Interface.__init__(self)
        self.user = user
        self.input_texts = {'message':''}
        self.current_date_message = datetime.now()
        self.active_input = None  # Pour suivre le champ de texte actif
        
    def add_message(self, input_text, auteur, heure, id_channel):
        sql = "INSERT INTO message(text,auteur,heure,id_channel) VALUES (%s,%s,%s,%s);"
        self.execute_sql(sql, (input_text, auteur, heure, id_channel))
        
    def three_last_messages(self):
        sql = "SELECT text, auteur, heure FROM notification ORDER BY heure DESC LIMIT 3"
        self.fetch_all(sql, ())
        
    def message_display(self, message, x_message, y_message, largeur_message, hauteur_message, radius_message):
        self.solid_rect_radius(self.light_grey, x_message, y_message, largeur_message, hauteur_message, radius_message)
        self.text(15, self.user, self.black, x_message, y_message - 30)
        self.text(14, self.current_date_message, self.white, x_message + 30, y_message - 30)
        self.text(13, message, self.white, x_message + 30, y_message + 30)
    
    # def event_writting_message(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()           
    #         elif event.type == pygame.KEYDOWN:
    #             if self.active_input:
    #                 if event.key == pygame.K_BACKSPACE:
    #                     self.input_texts[self.active_input] = self.input_texts[self.active_input][:-1]                        
    #                 else:
    #                     self.input_texts[self.active_input] += event.unicode
        
        
