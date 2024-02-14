import pygame
import re
from files.class_py.user import User
from files.class_py.interface import Interface

class Inscription(Interface, User):
    def __init__(self):
        Interface.__init__(self)
        User.__init__(self)
        self.page_inscription = True
        self.selected_rect = None
        self.register_run = True
        self.verif_connect = False
        self.error_message_register = ""

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
                        if (self.input_texts['email'] != '' and
                            self.input_texts['pseudo'] != '' and
                            self.input_texts['password'] != ''):                        
                                self.add_user(self.input_texts['pseudo'], self.input_texts['email'], self.input_texts['password'], 1)
                                print("click, user ajoutée avec succès !")
                                # self.verif_connect = True
                        else:
                            print("erreur register")
                            self.error_message_register = "Erreur, vous devez remplir toute les cases pour l'inscription"
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
                                print("click, user ajoutée avec succès !")
                            else:
                                print("Adresse e-mail non valide. Veuillez réessayer.")
                        else:
                            self.error_message_register = "Erreur, vous devez remplir toute les cases pour l'inscription"

                    elif self.is_mouse_over_button(pygame.Rect(370,520,280,20)): #Bouton 'Vous avez déjà un compte?'
                        self.register_run = False
                                                             
                    
                                
    def draw_error_message_register(self):
        if self.error_message_register:            
            self.text_align(18, self.error_message_register, self.pur_red, 525, 490) 
                        
        
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
        pass