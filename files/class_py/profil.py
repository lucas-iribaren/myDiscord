import pygame
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.notification import Notification

class Profil(Interface):
    def __init__(self, user):
        super().__init__()  # Call the constructor of the parent class 
        self.profil_run = False  # Initialize profil_run to False to enter the main loop
        self.private_chanels = False
        self.user = user
        self.channel_message = "Veuillez choisir un serveur."
        self.message = Message(self.user)
        self.notification = Notification(self.user)
        self.active_input = None  # Follow the active text field
        self.input_texts_message = {'message':''}        

    def create_profile_page(self):
        # Fill the screen in gray
        self.Screen.fill(self.dark_grey)

        # Add a logo
        self.img(550, 270, 100, 100, "icones/logo")
        self.text(25, self.channel_message, self.white, 435, 320)

        # Draw channels area
        self.rect_pv_chanel()
        
    def rect_server(self):
        # Servers area
        self.solid_rect(self.grey, 0, 0, 70, 1000)
        
    def create_server(self):
        # Coordonates of "Créer un serveur" 
        circle_center = (35, 35)
        circle_radius = 28
        
        # Verify if the mouse is hover the button
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5
        
        if distance_to_circle <= circle_radius:
            # Hover of the circle - Change the color
            pygame.draw.circle(self.Screen, self.blue, circle_center, circle_radius + 2)  # Circle
            # Draw the cross - hover
            pygame.draw.line(self.Screen, self.light_grey, (15, 35), (53, 35), 3)  # Horizontal line
            pygame.draw.line(self.Screen, self.light_grey, (35, 55), (35, 15), 3)  # Vertical line
            self.img(130, 30, 130, 40, "icones/text_area_hover")
            self.text(20, "Créer un serveur", self.white, 80, 20)
        else:
            # Wihtout hover
            pygame.draw.circle(self.Screen, self.light_grey, circle_center, circle_radius)
            # Draw cross - without hover
            pygame.draw.line(self.Screen, self.blue, (15, 35), (53, 35), 3)  # Horizontal line
            pygame.draw.line(self.Screen, self.blue, (35, 55), (35, 15), 3)  # Vertical line

    def private_server(self):
        # Coordonate button : "Messages privés"
        circle_center = (35, 100)
        circle_radius = 28

        # Verify if the mouse is hover the circle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5

        if distance_to_circle <= circle_radius:
            # Hover of the circle - Change the color of the icon
            pygame.draw.circle(self.Screen, self.blue, circle_center, circle_radius + 2)
            self.img(35, 100, 50, 50, "icones/avatar_2")
            self.img(130, 100, 140, 40, "icones/text_area_hover") # Text area
            self.text(20, "Messages privés", self.white, 85, 90)

            # Verify if the mouse is cliqued
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button ==  1:
                    self.private_chanels = not self.private_chanels  # Toggle the display of the private channels area
                    # if self.private_chanels:
                    #     self.channel_message = "Veuillez sélectionner un channel." # Change le message lorsque le bouton est cliqué
                    # else:
                    #     self.channel_message = "Veuillez choisir un serveur." # Rétablit le message par défaut lorsque le bouton est cliqué à nouveau
        else:
            # Without hover
            self.img(35, 100, 50, 50, "icones/avatar_0")

    def disconnect_button(self):
        # Coordonate button : "Se déconnecter"
        circle_center = (35, 100)
        circle_radius = 28

        # Verify if the mouse is hover the circle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5

        if distance_to_circle <= circle_radius:
            # Hover of the circle - Change the color of the icon
            pygame.draw.circle(self.Screen, self.blue, circle_center, circle_radius + 2)
            self.img(35, 550, 50, 50, "icones/disconnect")
            self.img(130, 100, 140, 550, "icones/text_area_hover") # Text area
            self.text(20, "Se déconnecter", self.white, 85, 90)

            # Verify if the mouse is cliqued
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button ==  1:
                    self.private_chanels = not self.private_chanels  # Toggle the display of the private channels area
        else:
            # Without hover
            self.img(35, 100, 50, 50, "icones/disconnect")    
            
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
        self.message.add_message(self.message.input_texts['message'], self.user, self.message.current_date_message,1)
        self.message.message_display(350,250,300,200,7)
                

    def rect_pv_chanel(self):
        # Draw private channels area
        if self.private_chanels:
            self.solid_rect(self.grey, 80, 0, 130, 1000) # Channels area
            self.solid_rect_radius(self.black, 80, 0, 130, 30, 5) # Title of the area
            self.text(20, "Messages Privés", self.white, 90, 5) # Title
    

    def home_profil(self):
        self.profil_run = True
        while self.profil_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.profil_run = False  # Exit the loop when the QUIT event is detected

            self.create_profile_page()
            self.rect_server()
            self.create_server()
            self.private_server()
            self.update()