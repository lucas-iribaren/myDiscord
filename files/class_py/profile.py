import pygame
from pygame.locals import *
from files.class_py.Interface import Interface
from files.class_py.message import Message
from files.class_py.notification import Notification
from files.class_py.Database import Database  
from files.class_py.SqlManager import SqlManager

class Profile(Interface, SqlManager):
    def __init__(self, user):
        super().__init__()  # Call the constructor of the parent class 
        self.profile_run = False  # Initialize profile_run to False to enter the main loop
        self.private_channels = False
        self.user = user
        print(self.user)
        self.channel_message = ""
        self.message = Message(self.user)
        self.notification = Notification()
        self.database = Database()
        self.author = None 
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60) / 1000
        self.message_sent = False
        self.active_input_mes = 0 
        self.input_message = ""        
        self.friend = ""
        self.usernames = self.retrieve_usernames()

    def create_profile_page(self):
        # Fill the screen in gray
        self.Screen.fill(self.dark_grey)

        # Add a logo
        self.img(550, 270, 100, 100, "icones/logo")       
        
        self.text(25, self.channel_message, self.white, 435, 320)
        if self.private_channels:
            self.channel_message = "Veuillez choisir une conversation"
        elif self.private_channels and self.friend:
            self.channel_message = ""
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
                response = self.show_confirmation_dialog("Déconnexion", "Ëtes-vous sûre de vouloir vous déconnecter ?", buttons=("Oui", "Non"))
                if response == 0: # If the user click "Oui"
                    print("Déconnexion en cours...")
                else:
                    print("Annulation de la déconnexion.")
            self.mouse_was_pressed = mouse_pressed # Update the mouse button state 
        else:
            # Without hover
            pygame.draw.circle(self.Screen, self.light_grey, circle_center, circle_radius + 2)
            self.img(35, 550, 50, 50, "icones/disconnect_blue")  

    def show_confirmation_dialog(self, title, message, buttons=("Oui", "Non")):
        # Draw dialog background
        self.solid_rect_radius(self.black, 300, 200, 400, 200, 10)
        self.solid_rect_radius(self.white, 300, 200, 400, 200, 10)

        # Draw title
        self.text_align(24, "Déconnexion", self.blue, 500, 220)

        # Draw message
        self.text(18, "Ëtes-vous sûre de vouloir vous déconnecter ?", self.black, 320, 260)

        for i, button_text in enumerate(buttons):
            button_rect = pygame.Rect(350 + i * (80 + 20), 280, 80, 40)
            pygame.draw.rect(self.Screen, self.blue, button_rect) # Draw button background
            self.text(18, button_text, self.white, button_rect.centerx, button_rect.centery) # Draw button text

        pygame.display.flip()

        # Return the index of the clicked button
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_pos = event.pos
                    for i, _ in enumerate(buttons):
                        button_rect = pygame.Rect(350 + i * (80 + 20), 280, 80, 40)
                        if button_rect.collidepoint(mouse_pos):
                            return i
            
    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.profile_run = False
                pygame.quit()
                quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                              
                if self.is_mouse_over_button(pygame.Rect(250, 530, 500, 50)):
                    self.active_input_mes = 1
                if self.is_mouse_over_button(pygame.Rect(760, 530, 50, 50)):
                    if self.input_message != "":
                        self.button_send(self.input_message)                        
                        self.input_message = ""
                        self.active_input_mes = 0
                    else:
                        print("Veuillez saisir un message.")
                    
                elif self.private_channels:
                    if self.is_mouse_over_button(pygame.Rect(80,50,130,30)):
                        self.friend = ""
                    elif self.is_mouse_over_button(pygame.Rect(80, 90, 130, 30)):
                        self.friend = "Lucy"
                    elif self.is_mouse_over_button(pygame.Rect(80, 130, 130, 30)):
                        self.friend = "Lucas"
                    elif self.is_mouse_over_button(pygame.Rect(80, 170, 130, 30)):
                        self.friend = "Valentin"
                    elif self.is_mouse_over_button(pygame.Rect(80, 210, 130, 30)):
                        self.friend = "Chiara"
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_message = self.input_message[:-1]
                elif event.key == pygame.K_RETURN:
                    if self.input_message != "":
                        self.button_send(self.input_message)                        
                        self.input_message = ""
                        self.active_input_mes = 0
                    else:
                        print("Veuillez saisir un message.")  
                else:
                    self.input_message += event.unicode

                                                                 

    def text_input(self):
        self.solid_rect_radius(self.light_grey, 250, 530, 500, 50, 10)
        self.text(16, self.input_message, self.black, 260, 535)        
        
    def rect_button_send(self):
        if self.is_mouse_over_button(pygame.Rect(760, 530, 50, 50)):
            self.solid_rect_radius(self.blue, 760, 530, 50, 50, 8)
            self.light_rect_radius(self.black,760, 530, 50, 50,1, 8)
        else:
            self.solid_rect_radius(self.light_grey, 760, 530, 50, 50, 8)


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
            
    def display_user(self):
        self.solid_rect_radius(self.black, 80, 50, 130, 30, 3)
        self.text_align(19,"Amis", self.white, 140, 65)     
        self.solid_rect_radius(self.dark_grey, 80, 90, 130, 30, 3)
        self.text_align(17, "Lucy", self.light_grey, 140, 100)
        self.solid_rect_radius(self.dark_grey, 80, 130, 130, 30, 3)
        self.text_align(17, "Lucas", self.light_grey, 140, 140)
        self.solid_rect_radius(self.dark_grey, 80, 170, 130, 30, 3)
        self.text_align(17, "Valentin", self.light_grey, 140, 180)
        self.solid_rect_radius(self.dark_grey, 80, 210, 130, 30, 3)
        self.text_align(17, "Chiara", self.light_grey, 140, 220)
        if self.is_mouse_over_button(pygame.Rect(80,50,130,30)):
            self.solid_rect_radius(self.white, 80, 50, 130, 30, 3)
            self.text_align(19,"Amis", self.black, 140, 65)
        elif self.is_mouse_over_button(pygame.Rect(80,90,130,30)):
            self.solid_rect_radius(self.light_grey,80,90,130,30,3)
            self.text_align(17, "Lucy", self.black, 140, 100)
        elif self.is_mouse_over_button(pygame.Rect(80,130,130,30)):
            self.solid_rect_radius(self.light_grey,80,130,130,30,3)
            self.text_align(17, "Lucas", self.black, 140, 140)
        elif self.is_mouse_over_button(pygame.Rect(80,170,130,30)):
            self.solid_rect_radius(self.light_grey, 80, 170, 130, 30, 3)
            self.text_align(17, "Valentin", self.black, 140, 180)
        elif self.is_mouse_over_button(pygame.Rect(80,210,130,30)):
            self.solid_rect_radius(self.light_grey, 80, 210, 130, 30, 3)
            self.text_align(17, "Chiara", self.black, 140, 220)             
                
    def retrieve_usernames(self):
        sql = "SELECT pseudo FROM user;"
        self.users = self.database.fetch_all(sql,())
        return [user[0] for user in self.users] if self.users else []
    
    def retrieve_user_role(self, username):
        sql = "SELECT id_role FROM user WHERE pseudo = %s;"
        user_role = self.database.fetch_one(sql, (username,))
        return user_role[0] if user_role else None

    def home_profile(self):
        self.profile_run = True
        while self.profile_run:                       
            self.create_profile_page()
            self.rect_server()
            self.create_server()
            self.disconnect_button()
            self.private_server()
            self.event_handling()                                   
            
            if self.private_channels:                       
                if self.friend:  # if a friend is clicked
                    self.channel_message = ""
                    self.text_input()
                    self.rect_button_send()
                    self.solid_rect_radius(self.grey, 230, 10, 90, 35, 3)
                    self.text(22, self.friend, self.white, 240, 15)                    
            
            for index, username in enumerate(self.usernames):
                y_position = 30 + index * 30
                
                role_sql = self.retrieve_user_role(username)
                text_color = self.red if role_sql == 2 else self.white

                if self.is_mouse_over_button(pygame.Rect(850, y_position, 130, 30)):
                    self.solid_rect_radius(self.grey, 850, y_position, 130, 30, 2)
                    
                self.text(19, username, text_color, 865, (y_position + 5))             

            if self.private_channels:
                if self.message_sent:
                    self.last_msg = self.message.last_message()
                    self.message.message_display(self.last_msg, self.author, 450, 380, 150, 90, 5)                    
                
                self.notification.display_notification(self.message.three_last_messages())
                self.notification.update_after_notif(self.delta_time)
                self.display_user()                            
            self.update()  
  
 
  
