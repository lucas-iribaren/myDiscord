import pygame
from files.class_py.database import Database

class Message(Database):
    def __init__(self, user):         
        Database.__init__(self)
        self.user = user
        self.input_texts = {'message':''}
        self.active_input = None  # Pour suivre le champ de texte actif
        
    def add_message(self, input_text, auteur, heure, id_channel):
        sql = "INSERT INTO message(text,auteur,heure,id_channel) VALUES (%s,%s,%s,%s);"
        self.execute_sql(sql, (input_text, auteur, heure, id_channel))
    
    def event_writting_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()           
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts[self.active_input] = self.input_texts[self.active_input][:-1]                        
                    else:
                        self.input_texts[self.active_input] += event.unicode
        
        
