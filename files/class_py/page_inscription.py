import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface


class Inscription(Interface):
    def __init__(self):
        Interface.__init__(self)
        self.database = Database()
        self.page_inscription = True
        self.email_rect = pygame.Rect(390, 150, 280, 30)
        self.pseudo_rect = pygame.Rect(390, 200, 280, 30)
        self.selected_rect = None  # Pour suivre le bloc sélectionné
        self.active_input = None  # Pour suivre le champ de texte actif

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.email_rect.collidepoint(event.pos):
                    self.selected_rect = self.email_rect
                    self.active_input = 'email'
                elif self.pseudo_rect.collidepoint(event.pos):
                    self.selected_rect = self.pseudo_rect
                    self.active_input = 'pseudo'
                else:
                    self.selected_rect = None
                    self.active_input = None


        
    def inscription(self):
        while self.page_inscription:
            
            if self.page_inscription:
                self.event_type()
                self.Screen.fill(self.dark_grey)
                self.solid_rect_radius(self.grey,350,50,350,500,8)
                self.solid_rect_radius(self.light_grey,460,55,150,50,8)
                self.text(20,'Créer votre compte',self.black,470,68)
                self.solid_rect_radius(self.light_grey,390,150,280,30,5)#Bloc email
                if self.is_mouse_over_button(pygame.Rect(390,150,280,30)):
                    self.light_rect(self.black,390,150,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey,390,200,280,30,5)#Bloc pseudo 
                if self.is_mouse_over_button(pygame.Rect(390,200,280,30)):
                    self.light_rect(self.black,390,200,280,30,1)

                if self.selected_rect:
                    self.light_rect(self.black, self.selected_rect.x, self.selected_rect.y, self.selected_rect.width, self.selected_rect.height, 1)  # Rectangle visible

                self.update()
               
                