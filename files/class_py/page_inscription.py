import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface

class Page_incription(Database, Interface):
    def __init__(self):
        Database.__init__(self, "localhost", "root", "1478", "mydiscord")
        Interface.__init__(self)
        self.page_inscription_run = False
        self.input_texts = {'nom': '', 'prenom': '', 'mail': '', 'mot_de_passe': ''}  
        self.active_input = None
        
    def handle_events_for_register(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts[self.active_input] = self.input_texts[self.active_input][:-1]
                    elif event.key == pygame.K_TAB:
                        self.active_input = 'mot_de_passe' if self.active_input == 'nom' else 'nom'
                    elif event.key == pygame.K_RETURN:
                        if (self.input_texts['nom'] != '' and
                            self.input_texts['prenom'] != '' and
                            self.input_texts['mail'] != '' and
                            self.input_texts['mot_de_passe'] != '' and
                            self.is_mouse_over_button(pygame.Rect(320, 505))):
                            self.button_connect()
                    else:
                        self.input_texts[self.active_input] += event.unicode

        