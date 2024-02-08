import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.page_connexion import Page_Connexion


class Accueil(Interface, Page_Connexion):
    def __init__(self):
        Interface.__init__(self)
        Page_Connexion.__init__(self)        
        self.database = Database("localhost", "root", "1478", "mydiscord")
        self.input_texts = {'pseudo': '', 'password': ''}  
        self.active_input = None  
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts[self.active_input] = self.input_texts[self.active_input][:-1]
                    elif event.key == pygame.K_TAB:
                        self.active_input = 'password' if self.active_input == 'pseudo' else 'pseudo'
                    elif event.key == pygame.K_RETURN:
                        if self.active_input['pseudo'] is not None and self.active_input['password'] is not None:
                            self.button_connect()                                              
                    else:
                        self.input_texts[self.active_input] += event.unicode                 
                    
    def text_entry(self):
        self.solid_rect_radius(self.white, 320, 370, 220, 35)
        self.light_rect(self.black, 320, 370, 220, 35, 2)
        self.solid_rect_radius(self.white, 320, 445, 220, 35)
        self.light_rect(self.black, 320, 445, 220, 35, 2)
        
        self.text(16, self.input_texts['pseudo'], self.black, 225, 363)
        self.text(16, "*" * len(self.input_texts['password']), self.black, 225, 443)
    
    def button_connect(self):
        if self.verify_account_exist:
            self.accueil_run = False
            # profil.profil_run = True
        else:
           self.accueil_run = True
            # profil.profil_run = False 
        
    def home(self):
        self.accueil_run = True
        self.active_input = 'pseudo'  
        
        while self.accueil_run:
            self.handle_events()
            
            self.Screen.fill(self.dark_grey)
            
            self.img(330, 160, 230, 220, "icones/logo")
            self.text_align(70, "MyDiscord", self.white, 610, 160)
            
            self.text_align(19, "Pseudo", self.white, 240, 335)
            self.text_align(19, "Mot de passe", self.white, 255, 410)
            self.light_rect(self.light_grey, 485, 435, 670, 270, 5)
            
            self.text_entry()  # Appeler la fonction pour gérer la saisie de texte
            
            self.solid_rect_radius(self.blue, 320, 505, 220, 35)
            self.text_align(21, "Connexion", self.black, 320, 505)
            self.text_align(21, "Ou", self.white, 485, 430)
            
            self.solid_rect_radius(self.blue, 650, 430, 220, 35)
            self.text_align(21, "Inscription", self.black, 650, 430)

            self.update()
