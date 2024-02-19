import pygame
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.notification import Notification
from files.class_py.user import User
from files.class_py.database import Database

class Profil(Interface):
    def __init__(self, user):
        super().__init__()  # Appelle le constructeur de la classe parente
        self.profil_run = False  # Initialise profil_run à False pour entrer dans la boucle principale
        self.private_channels = False
        self.user = user
        self.channel_message = "Veuillez choisir un serveur."
        self.message = Message(self.user)
        self.notification = Notification(self.user)
        self.user = User()
        self.database = Database()        
        self.input_message = self.message.input_texts_message['message']
        self.active_input = None  # Pour suivre le champ de texte actif

    def create_profile_page(self):
        # Remplit l'écran avec du gris
        self.Screen.fill((54, 57, 63))

        # Ajout du logo au milieu de la fenêtre
        self.img(550, 270, 100, 100, "icones/logo")
        self.text(25, self.channel_message, (249, 249, 249), 435, 320)

        # Dessine la zone des channels privés
        self.rect_pv_channel()

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

    def rect_pv_channel(self):
        # Dessine la zone des channels privés
        if self.private_channels:
            self.solid_rect((64, 68, 75), 80, 0, 90, 1000)

    def text_input(self):
        self.text(16, self.input_message, (249, 249, 249), 330, 150)

    def display_button(self):
        self.solid_rect((255, 255, 255), 330, 250, 50, 50)

    def display_member(self):
        self.user.display_user()

    def button_send(self):
        auteur = self.user
        if self.private_channels:
            self.message.add_message(self.input_message, auteur, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), 2)
            self.message.message_display(self.input_message, 350, 250, 300, 200, 7)
        elif not self.private_channels:
            self.message.add_message(self.input_message, auteur, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), 1)
            self.message.message_display(self.input_message, 350, 250, 300, 200, 7)
            
    def get_user_id(self):
        sql = "SELECT pseudo FROM user WHERE pseudo = %s" 
        result = self.database.fetch_one(sql, (self.user,))
        if result:
            return result[1]
        else:
            return None

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_message[self.active_input] = self.input_message[self.active_input][:-1]
                    else:
                        self.input_message[self.active_input] += event.unicode
                        
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_mouse_over_button(pygame.Rect(330, 250, 50, 50)):
                    if self.input_message is not None:
                        self.button_send()
                        print('envoyé')
                    else:
                        print("je ne trouve pas la valeur d'input")
                elif event.button == 1:
                    self.private_server_toggle()

    def private_server_toggle(self):
        # Coordonnées du bouton "Serveurs privé"
        circle_center = (35, 100)
        circle_radius = 28

        # Vérifie si la souris survole le cercle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5

        # Dessine toujours le bouton, mais change sa couleur si le survol a lieu
        if distance_to_circle <= circle_radius:
            # Survol du cercle - Change la couleur de l'icone
            pygame.draw.circle(self.Screen, (114, 137, 218), circle_center, circle_radius + 2)
            self.img(35, 100, 50, 50, "icones/avatar_2")
            self.img(130, 100, 110, 40, "icones/zone_texte_survol") # Zone texte directionnel
            self.text(20, "Messages privés", (249, 249, 249), 90, 90)

            # Vérifie si le bouton a été cliqué
            if pygame.mouse.get_pressed()[0]:
                self.private_channels = not self.private_channels  # Bascule l'affichage de la zone des channels privés
        else:
            # Sans survol
            pygame.draw.circle(self.Screen, (188, 186, 184), circle_center, circle_radius)
            self.img(35, 100, 50, 50, "icones/avatar_0")


    def home_profil(self):
        self.profil_run = True
        while self.profil_run:
            self.event_handling()
            self.create_profile_page()
            self.rect_server()
            self.create_server()
            self.display_button()
            self.text_input()
            self.update()
