import pygame
from files.class_py.user import User
from files.class_py.interface import Interface

class Inscription(Interface, User):
    def __init__(self):
        Interface.__init__(self)
        User.__init__(self)
        self.page_inscription = True
        self.email_rect = pygame.Rect(390, 170, 280, 30)
        self.pseudo_rect = pygame.Rect(390, 250, 280, 30)
        self.password_rect = pygame.Rect(390, 330, 280, 30)
        self.selected_rect = None  # Pour suivre le bloc sélectionné
        self.input_texts = {'email':'', 'pseudo': '', 'password':''}
        self.active_input = None  # Pour suivre le champ de texte actif
        self.register_run = True
        self.verif_connect = False
        self.error_message_register = ""

    def event_type(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            # Event keyboard
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts[self.active_input] = self.input_texts[self.active_input][:-1]
                    elif event.key == pygame.K_TAB:
                        if self.active_input == 'email':
                            self.active_input = 'pseudo'
                        elif self.active_input == 'pseudo':
                            self.active_input = 'password'
                        else:
                            self.active_input = 'email'
                    else:
                        self.input_texts[self.active_input] += event.unicode
                            
            # Event mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.email_rect.collidepoint(event.pos):
                        self.selected_rect = self.email_rect
                        self.active_input = 'email'
                    elif self.pseudo_rect.collidepoint(event.pos):
                        self.selected_rect = self.pseudo_rect
                        self.active_input = 'pseudo'
                    elif self.password_rect.collidepoint(event.pos):
                        self.selected_rect = self.password_rect
                        self.active_input = 'password'
                    else:
                        self.selected_rect = None
                        self.active_input = None
                        
                    if self.is_mouse_over_button(pygame.Rect(420,420,220,35)):
                        if (self.input_texts['email'] != '' and
                            self.input_texts['pseudo'] != '' and
                            self.input_texts['password'] != ''):                        
                                self.add_user(self.input_texts['pseudo'], self.input_texts['email'], self.input_texts['password'], 1)
                                print("click, user ajoutée avec succès !")
                                # self.verif_connect = True
                        else:
                            print("erreur register")
                            self.error_message_register = "Erreur, vous devez remplir toute les cases pour l'inscription"
                                
    def draw_error_message_register(self):
        if self.error_message_register:            
            self.text_align(18, self.error_message_register, self.pur_red, 525, 490)            
                        
        
    def register(self):
        while self.register_run:
            if self.page_inscription:
                self.event_type()
                self.Screen.fill(self.dark_grey)
                self.solid_rect_radius(self.grey,350,50,350,500,8)
                self.solid_rect_radius(self.light_grey,460,55,150,50,8)
                self.text(20,'Créer votre compte',self.black,470,68)                
                self.solid_rect_radius(self.blue,420,420,220,35,8)
                self.text_align(21,"S'inscrire ici !",self.black,530,436)
            
                # Draw email rectangle
                if self.is_mouse_over_button(pygame.Rect(390,170,280,30)):
                    self.light_rect(self.black,390,170,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey,390,170,280,30,5)#Bloc email
                self.text(19,"Email",self.white,390,140)
                # Draw pseudo rectangle
                if self.is_mouse_over_button(pygame.Rect(390,250,280,30)):
                    self.light_rect(self.black,390,250,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey, 390, 250, 280, 30, 5)#Bloc pseudo
                self.text(19,"Nom d'utilisateur",self.white,390,220)
                # Draw password rectangle
                if self.is_mouse_over_button(pygame.Rect(390,330,280,30)):
                    self.light_rect(self.black,390,330,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey, 390, 330, 280, 30, 5)#Bloc password
                self.text(19,"Mot de passe",self.white,390,300)
                
                self.draw_error_message_register()

                # Update text in selected rectangle
                if self.selected_rect:
                    self.light_rect(self.black, self.selected_rect.x, self.selected_rect.y, self.selected_rect.width, self.selected_rect.height, 1)  # Rectangle visible
                    # Display the current text on the selected rectangle
                    if self.active_input:
                        if self.active_input == 'email':
                            input_text = self.input_texts['email']
                        elif self.active_input == 'pseudo':
                            input_text = self.input_texts['pseudo']
                        elif self.active_input == 'password':
                            input_text = '*' * len(self.input_texts['password'])  # Display stars instead of password
                        self.text(15, input_text, self.black, self.selected_rect.x + 5, self.selected_rect.y + 5)

                self.update()

                if self.verif_connect:
                    #mettre la petite fenêtre qui apparaît quand on se connecte
                    pass

                    
                    

               
                