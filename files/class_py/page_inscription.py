import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface


class Inscription(Interface):
    def __init__(self):
        Interface.__init__(self)
        self.database = Database()
        self.input_texts = {'nom_utilisateur': '', 'password': ''}  
        self.active_input = None
        self.error_message = ""
        self.home_accueil = True 
        
    def event_type(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            # Event keyboard
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts[self.active_input] = self.input_texts[self.active_input][:-1]
                    elif event.key == pygame.K_TAB:
                        self.active_input = 'password' if self.active_input == 'nom_utilisateur' else 'nom_utilisateur'
                    else:
                        self.input_texts[self.active_input] += event.unicode
                            
            # Event mouse          
            elif event.type == pygame.MOUSEBUTTONUP: 
                if self.is_mouse_over_button(pygame.Rect(320, 505, 220, 35)):
                    pass
                     


        
    def inscription(self):
        self.page_inscription = True
        while self.page_inscription:
            
            if self.home_accueil:
                self.event_type()
                self.Screen.fill(self.dark_grey)
                self.solid_rect_radius(self.grey,350,50,350,500,8)
                self.solid_rect_radius(self.light_grey,460,55,150,50,8)
                self.text(20,'Créer votre compte',self.black,470,68)
                self.solid_rect_radius(self.light_grey,390,150,280,30,5)#Bloc email
                if self.is_mouse_over_button(pygame.Rect(390,150,280,30)):
                    self.light_rect(self.black,390,150,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey,390,200,280,30,5)
                if self.is_mouse_over_button(pygame.Rect(390,200,280,30)):
                    self.light_rect(self.black,390,200,280,30,1)
                self.update()
               
                