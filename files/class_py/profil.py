import pygame
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.notification import Notification
from files.class_py.user import User

class Profil(Interface):
    def __init__(self, user):
        super().__init__()
        self.profil_run = False
        self.private_channels = False
        self.user = user
        self.channel_message = "Veuillez choisir un serveur."
        self.message = Message(self.user)
        self.notification = Notification(self.user)
        self.user = User(self.user)
        self.active_input = None
        self.input_texts_message = {'message': ''}  # Initialisation avec une chaîne vide

    def create_profile_page(self):
        self.Screen.fill((54, 57, 63))
        self.img(550, 270, 100, 100, "icones/logo")
        self.text(25, self.channel_message, (249, 249, 249), 435, 320)
        self.rect_pv_channel()
        # Mise à jour de self.channel_message en fonction de self.private_channels
        if self.private_channels:
            self.channel_message = "Veuillez sélectionner un channel."
        else:
            self.channel_message = "Veuillez choisir un serveur."

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
                    self.private_channels = not self.private_channels  # Bascule l'affichage de la zone des channels privés
        else:
            # Sans survol
            self.img(35, 100, 50, 50, "icones/avatar_0")

    # def text_input(self):
    #     self.text(16, self.input_texts_message['message'], (249, 249, 249), 330, 150)

    def event_writing_message(self):
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
                        self.active_input = 'message'  # Mise à jour de self.active_input lors de la saisie du message

    # def display_button(self):
    #     self.solid_rect((255, 255, 255), 330, 250, 50, 50)

    # def button_send(self):
    #     auteur = self.user
    #     # Ajout de la vérification de self.private_channels pour décider du type de message à ajouter
    #     if self.private_channels:
    #         self.message.add_message(self.input_texts_message['message'], auteur, self.message.current_date_message, 2)
    #     else:
    #         self.message.add_message(self.input_texts_message['message'], auteur, self.message.current_date_message, 1)
    #     self.message.message_display(self.input_texts_message['message'], 350, 250, 300, 200, 7)

    def rect_pv_channel(self):  # Correction de la typo dans le nom de la méthode
        # Dessine la zone des channels privés
        if self.private_channels:
            self.solid_rect((64, 68, 75), 80, 0, 90, 1000)

    def home_profil(self):
        self.profil_run = True
        while self.profil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.profil_run = False

            self.create_profile_page()
            # self.rect_server()
            # self.create_server()
            self.private_server()
            # self.display_button()
            # self.text_input()
            self.event_writing_message()  
            # self.button_send()  
            self.update()

