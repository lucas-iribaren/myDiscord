import pygame
from pygame.locals import *
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.notification import Notification
from files.class_py.database import Database  
from files.class_py.user import User

class Profile(Interface):
    def __init__(self, user):
        super().__init__()  # Call the constructor of the parent class 
        self.profile_run = False  # Initialize profile_run to False to enter the main loop
        self.private_channels = False
        self.user = user
        print(self.user)
        self.channel_message = ""
        self.message = Message(self.user)
        self.notification = Notification()
        self.user_connected = User()
        self.database = Database()
        self.author = None 
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60) / 1000
        self.message_sent = False
        self.active_input_mes = 0 
        self.input_message = ""     
             

    def create_profile_page(self):
        # Fill the screen in gray
        self.Screen.fill(self.dark_grey)

        # Add a logo
        self.img(550, 270, 100, 100, "icones/logo")       
        
        self.text(25, self.channel_message, self.white, 435, 320)
        if self.private_channels:
            self.channel_message = "Veuillez choisir une conversation"
            self.text(25, self.channel_message, (249, 249, 249), 435, 320)
        else:
            self.channel_message = "Veuillez choisir un serveur"            
        self.rect_pv_channel()  

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

        # Check if the mouse is hovering over the circle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0]) ** 2 + (mouse_pos[1] - circle_center[1]) ** 2) ** 0.5

        # If the mouse is over the circle
        if distance_to_circle <= circle_radius:
            # Change the color of the circle
            pygame.draw.circle(self.Screen, (114, 137, 218), circle_center, circle_radius + 2)
            self.img(35, 100, 50, 50, "icones/avatar_2")
            self.img(130, 100, 140, 40, "icones/text_area_hover")  # Text area
            self.text(20, "Private Messages", self.white, 85, 90)

            # Check if the mouse button was initially pressed
            mouse_pressed = pygame.mouse.get_pressed()[0]
            if mouse_pressed and not self.mouse_was_pressed:
                self.private_channels = not self.private_channels  # Toggle the display of the private channels area
                # Add any other logic you want to execute on mouse click
            self.mouse_was_pressed = mouse_pressed  # Update the mouse button state
            # Hoover of the circle - Change the color of the icon
            pygame.draw.circle(self.Screen, self.blue, circle_center, circle_radius + 2)
            self.img(35, 100, 50, 50, "icones/avatar_2")
            self.img(130, 100, 140, 40, "icones/text_area_hover") # Text area
            self.text(20, "Messages privés", self.white, 85, 90)

        else:
            # Without hover
            self.img(35, 100, 50, 50, "icones/avatar_0")

    def disconnect_button(self):
        # Coordonate button : "Se déconnecter"
        circle_center = (35, 550)
        circle_radius = 28

        # Verify if the mouse is hover the circle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0]) ** 2 + (mouse_pos[1] - circle_center[1]) ** 2) ** 0.5

        # If the mouse is over the circle
        if distance_to_circle <= circle_radius:
            # Hover of the circle - Change the color of the icon
            pygame.draw.circle(self.Screen, self.blue, circle_center, circle_radius + 2)
            self.img(35, 550, 50, 50, "icones/disconnect_light_grey")
            self.img(130, 550, 140, 40, "icones/text_area_hover") # Text area
            self.text(20, "Se déconnecter", self.white, 85, 540)

            # Check if the mouse button was initially pressed
            mouse_pressed = pygame.mouse.get_pressed()[0]
            if mouse_pressed and not self.mouse_was_pressed:
                # Display a message box
                response = self.show_confirmation_dialog("Déconnexion", "Êtes-vous sûre de vouloir vous déconnecter ?", buttons=("Oui", "Non"))
                if response == 0: # If the user click "Oui"
                    print("Déconnexion en cours...")
                else:
                    print("Annulation de la déconnexion.") # If the user click "Non"
            self.mouse_was_pressed = mouse_pressed # Update the mouse button state 
        else:
            # Without hover
            pygame.draw.circle(self.Screen, self.light_grey, circle_center, circle_radius + 2)
            self.img(35, 550, 50, 50, "icones/disconnect_blue")  

    def show_confirmation_dialog(self, title, message, buttons=("Oui", "Non")):
        # Draw dialog background
        self.solid_rect_radius(self.light_grey, 300, 200, 400, 200, 10)

        # Draw title
        self.text_align(24, "Déconnexion", self.black, 500, 220)

        # Draw message
        self.text(18, "Êtes-vous sûre de vouloir vous déconnecter ?", self.black, 350, 260)

        # Define button width, height
        button_width =  60
        button_height =  35

        # Define specific positions for each button (x, y)
        button_positions = {
        "Oui": (350,  300),  # Position for "Oui" button
        "Non": (490,  330)   # Position for "Non" button
        }

        # Define specific positions for each text (x, y)
        text_positions = {
            "Oui": (370, 300),  # Position for "Oui" text
            "Non": (500, 330)   # Position for "Non" text
        }

        for button_text, (button_x, button_y) in button_positions.items():
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            pygame.draw.rect(self.Screen, self.blue, button_rect)  # Draw button background
        
            # Use the specific text position
            text_x, text_y = text_positions[button_text]
            self.text(18, button_text, self.white, text_x, text_y)  # Draw button text

        pygame.display.flip()

        # Return the index of the clicked button
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button ==   1:
                    mouse_pos = event.pos
                    for button_text, (button_x, button_y) in button_positions.items():
                        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                        if button_rect.collidepoint(mouse_pos):
                            return buttons.index(button_text)
                    
    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.profile_run = False
                pygame.quit()
                quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_mouse_over_button(pygame.Rect(250, 530, 500, 50)):
                    self.active_input_mes = 1
                 
            elif self.active_input_mes == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_message = self.input_message[:-1]  
                    else:
                        self.input_message += event.unicode            

                if self.is_mouse_over_button(pygame.Rect(760, 530, 50, 50)):
                    if self.input_message != "":
                        self.button_send(self.input_message)                        
                        self.input_message = ""
                        self.active_input_mes = 0
                    else:
                        print("Veuillez saisir un message.")
                        
                elif self.is_mouse_over_button(pygame.Rect(35, 100, 50, 50)):
                    self.notification.add_notification(self.message.three_last_messages())
                                      

    def text_input(self):
        self.solid_rect_radius(self.light_grey, 250, 530, 500, 50, 10)
        self.text(16, self.input_message, self.black, 260, 535)        
        
    def rect_button_send(self):
        if self.is_mouse_over_button(pygame.Rect(760, 530, 50, 50)):
            self.solid_rect_radius(self.dark_red, 760, 530, 50, 50, 8)
            self.light_rect_radius(self.black,750, 560, 50, 50,1, 8)
        else:
            self.solid_rect_radius(self.light_grey, 760, 530, 50, 50, 10)


    def button_send(self, message):
        self.author = self.user
        print("User:",self.author)
        if self.private_channels:
            self.message.add_message(message, self.author, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), 1)
        elif not self.private_channels:
            self.message.add_message(message, self.author, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), 1)
        message = ""
        self.message_sent = True
        print(self.message_sent)
        

    def rect_pv_channel(self):
        # Draw private channels area
        if self.private_channels:
            self.solid_rect(self.grey, 80, 0, 130, 1000) # Channels area
            self.solid_rect_radius(self.black, 80, 0, 130, 30, 5) # Title of the area
            self.text(20, "Messages Privés", self.white, 90, 5) # Title
    

    def home_profile(self):
        self.profile_run = True
        while self.profile_run:
            self.text_input()
            self.rect_button_send()
            self.event_handling()
            self.create_profile_page()
            self.rect_server()
            self.create_server()
            self.disconnect_button()
            self.private_server()                        
            if self.private_channels:
                if self.message_sent:
                    self.last_msg = self.message.last_message()
                    print("dernier message",self.last_msg)
                    self.message.message_display(self.last_msg, self.author, 450, 380, 150, 90, 5)
                    self.text_input()
                    self.rect_button_send()
                    self.notification.display_notification(self.message.three_last_messages())
                    self.notification.update_after_notif(self.delta_time) 
                else:
                    self.text_input()
                    self.rect_button_send()
                    self.notification.display_notification(self.message.three_last_messages())
                    self.notification.update_after_notif(self.delta_time)                                 
            self.update()  
