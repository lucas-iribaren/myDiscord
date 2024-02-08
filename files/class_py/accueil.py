import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface

class Accueil(Interface):
    def __init__(self):
        Interface.__init__(self)
        self.database = Database("localhost", "root", "1478", "mydiscord")
            
    def home(self):
        self.accueil_run = True        
        
        while self.accueil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                    
                    pygame.quit()
                    
            self.img(330, 160, 230, 220, "icones/logo")
            self.text_align(70, "MyDiscord", self.white, 610, 160)
            
            self.text_align(19, "Pseudo", self.white, 240, 335)
            self.solid_rect_radius(self.white, 320, 370, 220, 35)
            self.light_rect(self.black, 320, 370, 220, 35, 2)
            
            self.text_align(19, "Mot de passe", self.white, 255, 410)
            self.solid_rect_radius(self.white, 320, 445, 220, 35)
            self.light_rect(self.black, 320, 445, 220, 35, 2)
            self.light_rect(self.light_grey, 485, 435, 670, 270, 5)

            
            self.solid_rect_radius(self.blue, 320, 505, 220, 35)
            self.text_align(21, "Connexion", self.black, 320, 505)
            self.text_align(21, "Ou", self.white, 485, 430)
            
            self.solid_rect_radius(self.blue, 650, 430, 220, 35)
            self.text_align(21, "Inscription", self.black, 650, 430)

            self.update()
