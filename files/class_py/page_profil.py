import pygame
from interface import Interface 

class PageProfil(Interface):
    def __init__(self):
        super().__init__() # Appelle le constructeur de la classe parente

    def create_profile_page(self):
        # Remplir l'écran avec du gris
        self.Screen.fill((54, 57, 63))

        # Ajout du logo
        self.img(500, 250, 100, 100, "icones/logo")

        # Texte à afficher
        self.text(30, "Veuillez choisir un serveur", (249, 249, 249), 400, 300)

        # Mettre à jour l'affichage
        self.update()

pygame.init()
profil_page = PageProfil()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    profil_page.create_profile_page()
    
pygame.quit()