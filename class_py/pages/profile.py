import pygame
from pygame.locals import *
from class_py.pages.Interface import Interface
from class_py.communication.message import Message
from class_py.communication.notification import Notification
from class_py.database.SqlManager import SqlManager

class Profile(Interface, SqlManager):
    def __init__(self, user):
        Interface.__init__(self)
        SqlManager.__init__(self)# Call the constructor of the parent class 
        self.profile_run = False  # Initialize profile_run to False to enter the main loop
        self.private_messages= False
        self.server_gaming = False
        self.user = user
        self.channel_message = ""
        self.message = Message(self.user)
        self.notification = Notification()
        self.author = None 
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60) / 1000
        self.message_sent = False
        self.active_input_mes = 0 
        self.show_disconnect_dialog = False
        self.mouse_was_pressed = False
        self.input_message = ""
        self.input_message_channel = ""       
        self.friend = ""
        self.usernames = self.retrieve_usernames()
        self.channels = self.retrieve_channel()
        self.categories = self.retrieve_categorie()
        self.id_channel = self.message.id_channel_for_mes
        self.active_channel = False
        

    def create_profile_page(self):
        # Fill the screen
        self.Screen.fill(self.dark_grey)

        # Add a logo
        self.img(550, 270, 100, 100, "icones/logo")       
        
        self.text(25, self.channel_message, self.white, 435, 320)
        if self.private_messages:
            self.channel_message = "Veuillez choisir une conversation"
        elif self.private_messages and self.friend:
            self.channel_message = ""
            self.text(25, self.channel_message, (249, 249, 249), 435, 320)
        else:
            self.channel_message = "Veuillez choisir un serveur"            
        self.rect_pv_channel()  

        # Display disconnect dialog
        if self.show_disconnect_dialog:
            # Draw dialog background
            self.solid_rect_radius(self.light_grey,  300,  200,  400,  200,  10)

            # Draw title
            self.text_align(24, "Déconnexion", self.black,  500,  220)

            # Draw message
            self.text(18, "Êtes-vous sûre de vouloir vous déconnecter ?", self.black,  360,  260)

            # Draw button - "Oui"
            self.solid_rect_radius(self.dark_grey,  390,  300,  50,  30,  10)
            self.text_align(18, "Oui", self.white,  415,  315)

            # Draw button - "Non"
            self.solid_rect_radius(self.dark_grey,  540,  300,  50,  30,  10)
            self.text_align(18, "Non", self.white,  565,  315)

    def rect_server(self):
        # Servers area
        self.solid_rect(self.grey, 0, 0, 70, 1000)
        
    def public_server(self):
        # Coordonates of "Créer un serveur" 
        circle_center = (35, 35)
        circle_radius = 28
        
        # Verify if the mouse is hover the button
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0])**2 + (mouse_pos[1] - circle_center[1])**2) ** 0.5
        
        if distance_to_circle <= circle_radius:
            # Hover of the circle - Change the color
            pygame.draw.circle(self.Screen, self.blue, circle_center, circle_radius + 2)  # Circle
            self.img(35, 33, 50, 50, "icones/avatar_2")
            self.img(130, 30, 130, 40, "icones/text_area_hover")
            self.text(20, "Jeux-vidéo", self.white, 82, 20)
            
            mouse_pressed = pygame.mouse.get_pressed()[0]
            if mouse_pressed and not self.mouse_was_pressed:
                self.server_gaming = not self.server_gaming # Toggle the display of the private channels area
                if self.server_gaming and self.private_messages:
                    self.private_messages = False  # Deactivate private messages if server gaming is activated
            self.mouse_was_pressed = mouse_pressed  # Update the mouse button state
        else:
            # Wihtout hover
            pygame.draw.circle(self.Screen, self.grey, circle_center, circle_radius)
            self.img(35, 33, 50, 50, "icones/avatar_3")
                    

    def private_message(self):
        # Coordonate button : "Messages privés"
        circle_center = (35, 100)
        circle_radius = 28

        # Check if the mouse is hovering over the circle
        mouse_pos = pygame.mouse.get_pos()
        distance_to_circle = ((mouse_pos[0] - circle_center[0]) ** 2 + (mouse_pos[1] - circle_center[1]) ** 2) ** 0.5

        # If the mouse is over the circle
        if distance_to_circle <= circle_radius:
            # Check if the mouse button was initially pressed
            mouse_pressed = pygame.mouse.get_pressed()[0]
            if mouse_pressed and not self.mouse_was_pressed:
                self.private_messages = not self.private_messages # Toggle the display of the private channels area
                if self.private_messages and self.server_gaming: 
                    self.server_gaming = False  # Deactivate server gaming if private messages are activated
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
                self.show_disconnect_dialog = True
        else:
            # Without hover
            pygame.draw.circle(self.Screen, self.light_grey, circle_center, circle_radius + 2)
            self.img(35, 550, 50, 50, "icones/disconnect_blue")

    def dialog_disconnect(self):
        # Button - "Oui"
        if self.is_mouse_over_button(pygame.Rect(390,  300,  50,  30)) and self.show_disconnect_dialog: # Hoover
            self.solid_rect_radius(self.blue,  390,  300,  50,  30,  10)
            self.text_align(18, "Oui", self.white,  415,  315)
        
        # Button - "Non"
        if self.is_mouse_over_button(pygame.Rect(540,  300,  50,  30)) and self.show_disconnect_dialog: # Hoover
            self.solid_rect_radius(self.blue,  540,  300,  50,  30,  10)
            self.text_align(18, "Non", self.white,  565,  315)

    def clicked_disconnect_buttons(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]

        # Check if the mouse is clicking on "Oui" button
        if self.is_mouse_over_button(pygame.Rect(390,  300,  50,  30)) and self.show_disconnect_dialog:
            if mouse_pressed:
                from class_py.pages.home import Home
                home_instance = Home()
                home_instance.home()

        # Check if the mouse is clicking on "Non" button
        if self.is_mouse_over_button(pygame.Rect(540,  300,  50,  30)) and self.show_disconnect_dialog:
            if mouse_pressed:
                self.show_disconnect_dialog = False  # Close the disconnect dialog box

                    
    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.profile_run = False
                pygame.quit()
                quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                              
                if self.is_mouse_over_button(pygame.Rect(250, 530, 500, 50)):
                    self.active_input_mes = 1
                elif self.is_mouse_over_button(pygame.Rect(820, 530, 50, 50)):
                    if self.input_message_channel != "":
                        self.button_send(self.input_message_channel)                        
                        self.input_message_channel = ""
                        self.active_input_mes = 0
                    else:
                        print("Veuillez saisir un message.")                                      

                    
                elif self.private_messages:
                    if self.is_mouse_over_button(pygame.Rect(80,50,130,30)):
                        self.friend = ""
                    elif self.is_mouse_over_button(pygame.Rect(80, 90, 130, 30)):
                        self.friend = "Lucy"
                        self.id_channel = 12
                    elif self.is_mouse_over_button(pygame.Rect(80, 130, 130, 30)):
                        self.friend = "Lucas"
                        self.id_channel = 12
                    elif self.is_mouse_over_button(pygame.Rect(80, 170, 130, 30)):
                        self.friend = "Valentin"
                    elif self.is_mouse_over_button(pygame.Rect(80, 210, 130, 30)):
                        self.friend = "Chiara"
                        self.id_channel = 12
                                        
                elif self.server_gaming:
                    for index, channel in enumerate(self.channels[:2]):
                        y_channel = 35 + index * 30
                        if self.is_mouse_over_button(pygame.Rect(100, y_channel, 150, 30)):
                            self.id_channel = index + 1
                            print(self.id_channel)
                            self.active_channel = True

                    for index, channel in enumerate(self.channels[2:6]): # Channels 'Minecraft'
                        y_channel = 130 + index * 30
                        if self.is_mouse_over_button(pygame.Rect(100, y_channel, 150, 30)):
                            self.id_channel = index + 3
                            print(self.id_channel)
                            self.active_channel = True
                        
                    for index, channel in enumerate(self.channels[6:]): # Channels 'League Of Legends'
                        y_channel = 300 + index * 30
                        if self.is_mouse_over_button(pygame.Rect(100, y_channel, 150, 30)):
                            self.id_channel = index + 7
                            print(self.id_channel)
                            self.active_channel = True
                                       
                
            elif event.type == pygame.KEYDOWN:
                if self.active_input_mes == 1:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_message_channel = self.input_message_channel[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.input_message_channel != "":
                            self.button_send(self.input_message_channel)                        
                            self.input_message_channel = ""
                            self.active_input_mes = 0
                        else:
                            print("Veuillez saisir un message.")  
                    else:
                        self.input_message_channel += event.unicode

                        
                        
    # def input_write_user_display(self):
    #     messages = self.input_message_channel
    # # Récupère tous les messages
    #     if messages:
    #         print("je voit ton message")# Vérifie si le message est récupéré
    #         split_text = []
    #         line = ""
    #         for message in messages:
    #             print("je rentre dans le seconde for")
    #             words = message[1].split(" ")  # Divise le texte du message en mots
    #             for word in words:
    #                 print("je rentre dans le 3ème")
    #                 if len(line) + len(word) + 1 <= self.W:  # Vérifie si le mot peut être ajouté à la ligne actuelle
    #                     line += word + " "
    #                 else:
    #                     print("je suis dans le else et pas dans le 3ème")
    #                     split_text.append(line.strip())  # Ajoute la ligne complète à split_text
    #                     line = word + " "
    #             split_text.append(line.strip())  # Ajoute la dernière ligne
    #         # Maintenant, nous avons une liste de lignes de texte (split_text)
    #         # Nous allons afficher chaque ligne à une position spécifique sur l'écran
    #         y_position = 620  # Position verticale initiale
    #         for ligne in split_text:
    #             self.text(17, ligne, self.black, 510, y_position)  # Affiche la ligne
    #             y_position += 15  # Augmente la position verticale pour la prochaine ligne
                                                                    

    def text_input(self, message):
        self.solid_rect_radius(self.light_grey, 310, 530, 500, 50, 10)
        self.text(16, message, self.black, 320, 535)        
        
    def rect_button_send(self):
        if self.is_mouse_over_button(pygame.Rect(820, 530, 50, 50)):
            self.solid_rect_radius(self.blue, 820, 530, 50, 50, 8)
            self.light_rect_radius(self.black,820, 530, 50, 50,1, 8)
        else:
            self.solid_rect_radius(self.light_grey, 820, 530, 50, 50, 8)

    def button_send(self, message):
        self.author = self.user
        if self.private_messages:
            self.add_message(message, self.author, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), 11)
            message = ""
        elif self.server_gaming:
            self.add_message(message, self.author, self.message.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), self.message.channel_active)
        message = ""
        self.message_sent = True
        self.refresh_channel_messages()  # Update messages in the canal
        
        
    def rect_pv_channel(self):
        # Draw private channels area
        if self.private_messages:
            self.solid_rect(self.grey, 80, 0, 130, 1000) # Channels area
            self.solid_rect_radius(self.black, 80, 0, 130, 30, 5) # Title of the area
            self.text(20, "Messages Privés", self.white, 90, 5) # Title
        if self.server_gaming:
            self.solid_rect(self.grey, 80, 0, 200, 1000)
                                
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
        
    def refresh_channel_messages(self):
        # Call the method to verify the active channel and retrieve messages
        self.message.verify_id_category_for_display_messages(self.id_channel)
        # Call the method to display the messages in the active channel
        self.message.display_writed_message_channel() 
        
     

    def home_profile(self):
        self.profile_run = True
        while self.profile_run:                       
            self.create_profile_page()
            self.rect_server()
            self.public_server()            
            self.private_message()
            self.disconnect_button()
            self.dialog_disconnect()
            self.clicked_disconnect_buttons()
            self.event_handling()
            self.refresh_channel_messages()                                   
            if self.private_messages:
                self.display_user()                            
                if self.friend: # if a friend is clicked
                    self.channel_message = ""
                    self.text_input(self.input_message)
                    self.rect_button_send()
                    self.solid_rect_radius(self.grey, 230, 10, 90, 35, 3)
                    self.text(22, self.friend, self.white, 240, 15)
                    
            if self.server_gaming:
                self.solid_rect(self.grey, 890,0, 590,600) #bloc user
                if self.id_channel != 0:
                    self.solid_rect(self.grey, 290,0, 590,600) # Bloc message

                cat_welc = self.categories[0]
                cat_mc = self.categories[1]
                cat_lol = self.categories[2]
                
                if self.active_channel:
                    self.text_input(self.input_message_channel)
                    self.rect_button_send()
                    
                # 'Bienvenue'
                y_categorie_welc = 5 
                if self.is_mouse_over_button(pygame.Rect(100, y_categorie_welc, 160, 30)): 
                    self.solid_rect_radius(self.dark_grey, 100, y_categorie_welc, 160, 30, 2)  
                self.text(21, cat_welc, self.blue, 105, y_categorie_welc + 5)

                # 'Minecraft'
                y_categorie_mc = 100
                if self.is_mouse_over_button(pygame.Rect(100, y_categorie_mc, 160, 30)): 
                    self.solid_rect_radius(self.dark_grey, 100, y_categorie_mc, 160, 30, 2) 
                self.text(21, cat_mc, self.blue, 105, y_categorie_mc + 5)

                # 'League of Legends'
                y_categorie_lol = 270
                if self.is_mouse_over_button(pygame.Rect(100, y_categorie_lol, 160, 30)): 
                    self.solid_rect_radius(self.dark_grey, 100, y_categorie_lol, 160, 30, 2) 
                self.text(21, cat_lol, self.blue, 105, y_categorie_lol + 5)


                for index, channel in enumerate(self.channels[:2]): # Channels 'Bienvenue'
                    y_channel = 35 + index * 30
                    
                    if self.is_mouse_over_button(pygame.Rect(100, y_channel, 160, 30)): 
                        self.solid_rect_radius(self.dark_grey, 100, y_channel, 160, 30, 2)
                    self.text(19, channel, self.black, 105, y_channel + 5)

                for index, channel in enumerate(self.channels[2:6]): # Channels 'Minecraft'
                    y_channel = 130 + index * 30
                    
                    if self.is_mouse_over_button(pygame.Rect(100, y_channel, 160, 30)): 
                        self.solid_rect_radius(self.dark_grey, 100, y_channel, 160, 30, 2)
                    self.text(19, channel, self.black, 105, y_channel + 5)

                for index, channel in enumerate(self.channels[6:]): # Channels 'League Of Legends'
                    y_channel = 300 + index * 30
                    
                    if self.is_mouse_over_button(pygame.Rect(100, y_channel, 160, 30)): 
                        self.solid_rect_radius(self.dark_grey, 100, y_channel, 160, 30, 2)
                    self.text(19, channel, self.black, 105, y_channel + 5)

                self.message.verify_id_category_for_display_messages(self.id_channel)
                self.message.display_writed_message_channel()
                # display messages
                for index, username in enumerate(self.usernames):
                    y_position = 10 + index * 30
                    role_sql = self.retrieve_user_role(username)
                    roles_color = self.red if role_sql == 2 else self.white # if user is admin color red else black

                    if self.is_mouse_over_button(pygame.Rect(895, y_position, 100, 30)): 
                        self.solid_rect_radius(self.dark_grey, 895, y_position, 100, 30, 2)# hover pointed*

                    self.text(19, username, roles_color, 900, (y_position + 5)) # Text user 

            if self.active_channel:
                self.text(21, channel, self.blue, 300, 10)
            if self.message_sent:
                # if self.active_channel:
                #     self.last_msg_channel = self.get_latest_messages_by_channel(self.message.channel_active)
                #     self.message.message_display_channel(self.last_msg_channel, self.author, 300, 400)
                # if self.friend:
                #     self.message.message_display(self.input_message, self.author, 300, 500, 200, 50, 3)
                pass
            if not self.private_messages and not self.server_gaming:
                self.notification.display_notification(self.three_last_messages())
                self.notification.update_after_notif(self.delta_time)
                               
            self.update()  
  
 
  
