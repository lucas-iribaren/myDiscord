import pygame
from files.class_py.interface import Interface    


class PageProfil(Interface):
    def __init__(self):
        super().__init__() # Appelle le constructeur de la classe parente
        self.profil_run = True

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
        # Coordonnées du cercle
        circle_center = (38, 35)
        circle_radius = 28
        
        # Vérifier si la souris survole le cercle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5
        
        if distance_to_circle <= circle_radius:
            # Survole du cercle : change la couleur du bouton
            pygame.draw.circle(self.Screen, (114, 137, 218), circle_center, circle_radius + 2)  # Cercle
            # Dessin de la croix
            pygame.draw.line(self.Screen, (188, 186, 184), (20, 35), (58, 35), 3)  # Ligne horizontale
            pygame.draw.line(self.Screen, (188, 186, 184), (39, 55), (39, 15), 3)  # Ligne verticale
            self.text(20, "Créer un serveur", (249, 249, 249), 40, 30)
        else:
            # Sans survol
            pygame.draw.circle(self.Screen, (188, 186, 184), circle_center, circle_radius)  # Cercle normal
            # Dessin de la croix
            pygame.draw.line(self.Screen, (114, 137, 218), (20, 35), (58, 35), 3)  # Ligne horizontale
            pygame.draw.line(self.Screen, (114, 137, 218), (39, 55), (39, 15), 3)  # Ligne verticale

        # Mettre à jour l'affichage
        self.update()
        
    def home_profil(self):
        while self.profil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.profil_run = False
                    pygame.quit()

            self.create_profile_page()
            self.rect_server()
            self.create_server()
    
