import pygame
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.notification import Notification
from files.class_py.database import Database  
from files.class_py.user import User

class Profil(Interface):
    def __init__(self, user):
        super().__init__()  
        self.profil_run = False  
        self.private_channels = False  
        self.user = user
        print(self.user)
        self.channel_message = ""
        self.message = Message(self.user)
        self.notification = Notification()
        self.user_connected = User()
        self.database = Database()         
        self.auteur = None 
        self.clock = pygame.time.Clock()
        self.input_message = self.message.input_texts_message['message']
        self.delta_time = self.clock.tick(60) / 1000       

    def create_profile_page(self):
        self.Screen.fill((54, 57, 63))
        self.img(550, 270, 100, 100, "icones/logo")
        self.text(25, self.channel_message, (249, 249, 249), 435, 320)
        if self.private_channels:
            self.channel_message = "Veuillez choisir une conversation"
            self.text(25, self.channel_message, (249, 249, 249), 435, 320)
        else:
            self.channel_message = "Veuillez choisir un serveur"            
        self.rect_pv_channel()  

    def rect_server(self):
        self.solid_rect((64, 68, 75), 0, 0, 70, 1000)

    def create_server(self):
        circle_center = (35, 35)
        circle_radius = 28
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5
        
        if distance_to_circle <= circle_radius:
            pygame.draw.circle(self.Screen, (114, 137, 218), circle_center, circle_radius + 2) 
            pygame.draw.line(self.Screen, (188, 186, 184), (15, 35), (53, 35), 3)  
            pygame.draw.line(self.Screen, (188, 186, 184), (35, 55), (35, 15), 3)  
            self.img(130, 30, 130, 40, "icones/zone_texte_survol")
            self.text(20, "Créer un serveur", (249, 249, 249), 80, 20)
        else:
            pygame.draw.circle(self.Screen, (188, 186, 184), circle_center, circle_radius)
            pygame.draw.line(self.Screen, (114, 137, 218), (15, 35), (53, 35), 3)  
            pygame.draw.line(self.Screen, (114, 137, 218), (35, 55), (35, 15), 3)

    def private_server(self):  # Correction du nom de la méthode
        circle_center = (35, 100)
        circle_radius = 28
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5

        if distance_to_circle <= circle_radius:
            pygame.draw.circle(self.Screen, (114, 137, 218), circle_center, circle_radius + 2)
            self.img(35, 100, 50, 50, "icones/avatar_2")
            self.img(130, 100, 140, 40, "icones/zone_texte_survol")
            self.text(20, "Messages privés", (249, 249, 249), 85, 90)
            if pygame.mouse.get_pressed()[0]:
                self.private_channels = not self.private_channels
        else:
            self.img(35, 100, 50, 50, "icones/avatar_0")  

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_message = self.input_message[:-1]  
                else:
                    self.input_message += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_mouse_over_text_input(pygame.Rect(330, 150, 150, 80)):
                    self.active_input_mes = 'message'  
                else:
                    self.active_input_mes = None  

                if self.is_mouse_over_button(pygame.Rect(330, 250, 50, 50)):
                    if self.input_message != "":
                        self.button_send()
                        print('envoyé')
                    else:
                        print("Veuillez saisir un message.")
                        
                elif self.is_mouse_over_button(pygame.Rect(35, 100, 50, 50)):
                    self.notification.add_notification(self.message.three_last_messages())
                                        

    def text_input(self):
        self.solid_rect(self.white, 330, 150, 150, 80)
        self.text(16, self.input_message, self.pur_red, 330, 150)        
        
    def rect_button_send(self):
        self.solid_rect(self.white, 330, 250, 50, 60)

    def button_send(self):
        self.auteur = self.user
        print(self.auteur)
        if self.private_channels:
            self.message.add_message(self.input_message, self.auteur, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), 1)
        elif not self.private_channels:
            self.message.add_message(self.input_message, self.auteur, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), 1)
        self.message.message_display(self.input_message, self.auteur, 450, 380, 150, 90, 5)

    def rect_pv_channel(self):  
        if self.private_channels:
            self.solid_rect((64, 68, 75), 80, 0, 130, 1000) 
            self.solid_rect_radius((0, 0, 0), 80, 0, 130, 30, 5) 
            self.text(20, "Messages Privés", (249, 249, 249), 90, 5)

    def home_profil(self):
        self.profil_run = True
        while self.profil_run:
            self.event_handling()
            self.create_profile_page()
            self.rect_server()
            self.create_server()
            self.private_server()                        
            if self.private_channels:
                self.text_input()
                self.rect_button_send()
                self.message.message_display(self.input_message, self.auteur, 450, 380, 150, 90, 5)
                self.notification.display_notification(self.message.three_last_messages())                                 
            self.update() 
