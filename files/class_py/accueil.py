import pygame
# from files.class_py.database import Database
from files.class_py.interface import Interface

class Accueil(Interface):
    def __init__(self):
        super().__init__()
        # self.database = Database("localhost","root","1478","mydiscord")
            
    def home(self):
        self.accueil_run = True
        self.click_mouse = pygame
        
        while self.accueil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                    
                    pygame.quit()
            
            self.update()
