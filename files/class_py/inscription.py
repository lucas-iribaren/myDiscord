import pygame, time
import re
from files.class_py.user import User
from files.class_py.interface import Interface

class Inscription(Interface, User):
    def __init__(self):
        Interface.__init__(self)
        User.__init__(self)
        self.page_inscription = True
        self.input_texts = {'email':'', 'pseudo': '', 'password': ''}
        self.selected_rect = None
        self.register_run = True
        self.verif_connect = False
        self.error_message_register = ""
        self.email_rect = pygame.Rect(390, 170, 280, 30)
        self.pseudo_rect = pygame.Rect(390, 250, 280, 30)
        self.password_rect = pygame.Rect(390, 330, 280, 30)
        self.clock = pygame.time.Clock()
        self.error_timer = 0
        self.error_duration = 1000

    def is_valid_email(self, email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email) is not None
    
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
                    elif event.key == pygame.K_RETURN:
                        if (self.input_texts['email'] != '' and self.input_texts['pseudo'] != '' and self.input_texts['password'] != ''):
                            if self.is_valid_email(self.input_texts['email']):
                                self.add_user(self.input_texts['pseudo'], self.input_texts['email'], self.input_texts['password'], 1)
                                self.error_message_register = "Votre compte à bien été ajouté !"
                            else:
                                self.error_message_register = "Erreur, l'adresse mail n'est pas conforme."
                        else:
                            self.error_message_register = "Erreur, vous devez remplir toute les cases pour l'inscription."
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
                        
                    if self.is_mouse_over_button(pygame.Rect(420,420,220,35)): #Bouton 'inscription'
                        if (self.input_texts['email'] != '' and self.input_texts['pseudo'] != '' and self.input_texts['password'] != ''):
                            if self.is_valid_email(self.input_texts['email']):
                                self.add_user(self.input_texts['pseudo'], self.input_texts['email'], self.input_texts['password'], 1)
                                self.error_message_register = "Votre compte à bien été ajouté !"
                            else:
                                self.error_message_register = "Erreur, l'adresse mail n'est pas conforme."
                        else:
                            self.error_message_register = "Erreur, vous devez remplir toute les cases pour l'inscription."

                    elif self.is_mouse_over_button(pygame.Rect(370,520,280,20)): #Bouton 'Vous avez déjà un compte?'
                        self.register_run = False
                    else:
                        # Vérifier si le clic est sur l'un des rectangles d'entrée de texte
                        for input_rect in [(390,170,280,30), (390, 250, 280, 30), (390, 330, 280, 30)]:
                            if self.is_mouse_over_button(pygame.Rect(input_rect)):
                                # Garder en mémoire le rectangle cliqué précédemment et activer l'entrée de texte
                                self.clicked_rect = input_rect
                                self.active_input = 'email' if input_rect == (390, 170, 280, 30) else ('pseudo' if input_rect == (390, 250, 280, 30) else 'password')

    def draw_error_message_register(self):
        if self.error_message_register:
            self.solid_rect_radius(self.light_grey,620,20,360,55,8)
            self.text_align(16, self.error_message_register, self.pur_red, 796, 45)                  
            self.error_timer += self.clock.tick()
            if self.error_timer >= self.error_duration:
                self.error_message_register = None
                self.error_timer = 0

    def register(self):
        while self.register_run:
            if self.page_inscription:
                self.event_type()
                self.Screen.fill(self.dark_grey)#background
                self.solid_rect_radius(self.grey,350,50,350,500,8)#bloc inscription
                self.solid_rect_radius(self.light_grey,460,55,150,50,8)#bordure
                self.text(20,'Créer votre compte',self.black,470,68)                
                self.solid_rect_radius(self.blue,420,420,220,35,8)
                self.text_align(21,"S'inscrire ici !",self.black,530,436)


                #Bloc Email
                if self.is_mouse_over_button(pygame.Rect(390,170,280,30)):
                    self.light_rect(self.black,390,170,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey,390,170,280,30,5)#Bloc email
                self.text(19,"Email",self.white,390,140)

                #Bloc Pseudo
                if self.is_mouse_over_button(pygame.Rect(390,250,280,30)):
                    self.light_rect(self.black,390,250,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey, 390, 250, 280, 30, 5)#Bloc pseudo
                self.text(19,"Nom d'utilisateur",self.white,390,220)

                #Bloc Password
                if self.is_mouse_over_button(pygame.Rect(390,330,280,30)):
                    self.light_rect(self.black,390,330,280,30,1)#Curseur selectionné
                self.solid_rect_radius(self.light_grey, 390, 330, 280, 30, 5)#Bloc password
                self.text(19,"Mot de passe",self.white,390,300)
                
                if self.is_mouse_over_button(pygame.Rect(370,520,280,20)):
                    self.text_align(18,"Tu as déjà un compte?",self.black,435,520)
                else:
                    self.text_align(15,"Tu as déjà un compte?",self.black,435,520)
                    
                self.draw_error_message_register()
                self.select_input()
                
                if self.verif_connect:
                    pass
                #mettre la petite fenêtre qui apparaît quand on se connecte
                        
                self.update()

    def select_input(self):
        if self.selected_rect:
            self.light_rect(self.black, self.selected_rect.x, self.selected_rect.y,
                            self.selected_rect.width, self.selected_rect.height, 1)
            if self.active_input:
                input_text = self.input_texts[self.active_input]
                self.text(15, input_text, self.black, self.selected_rect.x + 5, self.selected_rect.y + 5)