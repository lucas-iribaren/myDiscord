import pygame
from interface import Interface

class PageProfil(Interface):
    def __init__(self):
        super().__init__() # Appelle le constructeur de la classe parente

    def create_profile_page(self):
        # Remplir l'écran avec du gris
        self.Screen.fill((54, 57, 63)) # Couleur grise

        # Ajouter une image au-dessus du texte
        image_name = "Logo"
        image_x = self.W // 2 # Centre horizontalement
        image_y = self.H // 2 # Centre verticalement
        image_largeur = 200 # Largeur de l'image
        image_hauteur = 200 # Hauteur de l'image
        self.logo(image_x, image_y, image_largeur, image_hauteur, image_name)

        # Texte à afficher
        texte_content = "Mon Profil"
        texte_size = 40
        color = (249, 249, 249) # Couleur blanche

        # Obtenir la police
        font = self.font()

        # Position du texte centré
        x = self.W // 2
        y = self.H // 2 + image_hauteur // 2

        # Afficher le texte centré
        self.text_align(texte_size, texte_content, color, x, y, font)

        # Mettre à jour l'affichage
        self.update()

if __name__ == "__main__":
    pygame.init()
    profil_page = PageProfil()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        profil_page.create_profile_page()
    
    pygame.quit()