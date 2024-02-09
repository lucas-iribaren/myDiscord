import pygame
from interface import Interface 

class PageProfil(Interface):
    def __init__(self):
        super().__init__() # Appelle le constructeur de la classe parente

    def create_profile_page(self):
        # Remplir l'écran avec du gris
        self.Screen.fill((54, 57, 63))

        # Ajout du logo
        self.img(550, 270, 100, 100, "icones/logo")

        # Texte à afficher
        self.text(25, "Veuillez choisir un serveur.", (249, 249, 249), 450, 320)

    def rect_server(self):
        # Zone des serveurs
        self.solid_rect(30, 100, 90, 1000, (64, 68, 75))

    def create_server(self):
        # Bouton créer un serveur
        pygame.draw.circle(self.Screen, (188, 186, 184), (38, 35), 28)  # Dessin cercle
        pygame.draw.line(self.Screen, (114, 137, 218), (20, 35), (58, 35), 3) # Dessin ligne horizontal de la croix
        pygame.draw.line(self.Screen, (114, 137, 218), (39, 55), (39, 15), 3) # Dessin ligne vertical de la croix

pygame.init()
profil_page = PageProfil()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    profil_page.create_profile_page()
    profil_page.rect_server()
    profil_page.create_server()
    profil_page.update()
    
pygame.quit()