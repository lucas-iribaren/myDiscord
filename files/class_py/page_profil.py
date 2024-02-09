import pygame
from files.class_py.interface import Interface    
pygame.init()


class PageProfil(Interface):
    def __init__(self):
        super().__init__() # Appelle le constructeur de la classe parente
        self.profil_run = True

    def create_profile_page(self):
        # Remplir l'écran avec du gris
        self.Screen.fill((54, 57, 63))

        # Ajout du logo
        self.img(500, 250, 100, 100, "icones/logo")

        # Texte à afficher
        self.text(30, "Veuillez choisir un serveur", (249, 249, 249), 400, 300)

        # Mettre à jour l'affichage
        self.update()
        
    def home_profil(self):
        while self.profil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.profil_run = False
                    pygame.quit()

            self.create_profile_page()
        



    
