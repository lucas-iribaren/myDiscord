import pygame
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.accueil import Accueil
accueil = Accueil()

class Profil(Interface):
    def __init__(self):
        super().__init__()  # Appelle le constructeur de la classe parente
        self.profil_run = False  # Initialise profil_run à False pour entrer dans la boucle principale
        self.private_chanels = False
        self.channel_message = "Veuillez choisir un serveur."
        self.message = Message()
        self.active_input = None  # Pour suivre le champ de texte actif
        self.input_texts_message = {'message':''}        

    def create_profile_page(self):
        # Remplit l'écran avec du gris
        self.Screen.fill((54, 57, 63))

        # Ajout du logo au milieu de la fenêtre
        self.img(550, 270, 100, 100, "icones/logo")
        self.text(25, self.channel_message, (249, 249, 249), 435, 320)

        # Dessine la zone des channels privés
        self.rect_pv_chanel()
        
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
            self.text(20, "Messages privés", (249, 249, 249), 90, 90)

            # Vérifie si le bouton a été cliqué
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  1:
                    self.private_chanels = not self.private_chanels  # Bascule l'affichage de la zone des channels privés
                    # if self.private_chanels:
                    #     self.channel_message = "Veuillez sélectionner un channel." # Change le message lorsque le bouton est cliqué
                    # else:
                    #     self.channel_message = "Veuillez choisir un serveur." # Rétablit le message par défaut lorsque le bouton est cliqué à nouveau
        else:
            # Sans survol
            self.img(35, 100, 50, 50, "icones/avatar_0")
            
    def event_writting_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()           
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts_message[self.active_input] = self.input_texts_message[self.active_input][:-1]                        
                    else:
                        self.input_texts_message[self.active_input] += event.unicode
            
    def button_send(self):
        self.message.add_message(self.message.input_texts_message['message'], accueil.user_data, self.message.curent_time,1)
        self.message.message_display(350,250,300,200,7)
                

    def rect_pv_chanel(self):
        # Dessine la zone des channels privés
        if self.private_chanels:
            self.solid_rect((64, 68, 75), 80, 0, 90, 1000)
    

    def home_profil(self):
        self.profil_run = True
        while self.profil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.profil_run = False  # Sort de la boucle lorsque l'événement QUIT est détecté

            self.create_profile_page()
            self.rect_server()
            self.create_server()
            self.private_server()
            self.update() 

        pygame.quit()