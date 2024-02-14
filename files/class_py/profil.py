import pygame
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.notification import Notification   


class Profil(Interface):
    def __init__(self, user):
        super().__init__()  # Appelle le constructeur de la classe parente
        self.user = user
        self.profil_run = False  # Initialise profil_run à False pour entrer dans la boucle principale
        self.message = Message(self.user)
        self.notification = Notification(self.user)

    def create_profile_page(self):
        # Remplit l'écran avec du gris
        self.Screen.fill((54, 57, 63))

        # Ajout du logo au milieu de la fenêtre
        self.img(550, 270, 100, 100, "icones/logo")
        self.text(25, "Veuillez choisir un serveur.", (249, 249, 249), 450, 320)
        
    def rect_server(self):
        # Zone des serveurs
        self.solid_rect((64, 68, 75), 0, 0, 70, 1000)
        
    def create_server(self):
        # Coordonnées du bouton "Créer un serveur"
        circle_center = (35, 35)
        circle_radius = 28
        
        # Vérifie si la souris survole le bouton
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5
        
        if distance_to_circle <= circle_radius:
            # Survol du cercle - Change la couleur du bouton
            pygame.draw.circle(self.Screen, (114, 137, 218), circle_center, circle_radius + 2)  # Cercle
            # Dessin de la croix - Survol
            pygame.draw.line(self.Screen, (188, 186, 184), (15, 35), (53, 35), 3)  # Ligne horizontale
            pygame.draw.line(self.Screen, (188, 186, 184), (35, 55), (35, 15), 3)  # Ligne verticale
            self.img(130, 30, 130, 40, "icones/zone_texte_survol")
            self.text(20, "Créer un serveur", (249, 249, 249), 80, 20)
        else:
            # Sans survol
            pygame.draw.circle(self.Screen, (188, 186, 184), circle_center, circle_radius)
            # Dessin de la croix - Sans survol
            pygame.draw.line(self.Screen, (114, 137, 218), (15, 35), (53, 35), 3)  # Ligne horizontale
            pygame.draw.line(self.Screen, (114, 137, 218), (35, 55), (35, 15), 3)  # Ligne verticale

    def private_server(self):
        # Coordonnées du bouton "Serveurs privé"
        circle_center = (35, 100)
        circle_radius = 28

        # Vérifie si la souris survole le cercle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5

        if distance_to_circle <= circle_radius:
            # Survol du cercle - Change la couleur de l'icone
            pygame.draw.circle(self.Screen, (114, 137, 218), circle_center, circle_radius + 2)
            self.img(35, 100, 50, 50, "icones/avatar_2")
            self.img(130, 100, 110, 40, "icones/zone_texte_survol") # Zone texte directionnel
            self.text(20, "Serveur privé", (249, 249, 249), 90, 90)
        else:
            # Sans survol
            self.img(35, 100, 50, 50, "icones/avatar_0")

    def home_profil(self):
        self.profil_run = True
        while self.profil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.profil_run = False  # Sort de la boucle lorsque l'événement QUIT est détecté
                    pygame.quit()

            self.create_profile_page()
            self.rect_server()
            self.create_server()
            self.private_server()
            self.update()  
