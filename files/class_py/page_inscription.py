import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.accueil import Accueil
accueil = Accueil()
database = Database("localhost", "root", "1478", "mydiscord")

class Page_incription(Database, Interface):
    def __init__(self):
        Database.__init__(self, "localhost", "root", "1478", "mydiscord")
        Interface.__init__(self)
        self.page_inscription_run = False
        self.input_texts = {"Email": '', "nom_d'utilisateur": '',  "mot_de_passe": ''}  
        self.active_input = None
        
    def handle_events_for_register(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_texts[self.active_input] = self.input_texts[self.active_input][:-1]
                    elif event.key == pygame.K_TAB:
                        self.active_input = 'mot_de_passe' if self.active_input == 'nom' else 'nom'
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.is_mouse_over_button(pygame.Rect(320, 505)):
                            if (self.input_texts['mail'] != '' and
                                self.input_texts['nom_utilisateur'] != '' and  # Correction du nom de la clé
                                self.input_texts['mot_de_passe'] != ''):      
                                    pseudo = self.input_texts['nom_utilisateur']  # Correction du nom de la clé
                                    mail = self.input_texts['mail']
                                    password = self.input_texts['mot_de_passe']
                                    id_role = 3

                                # Génération et exécution de la requête SQL pour insérer les données dans la base de données
                                    query = "INSERT INTO user(pseudo, mail, password, id_role) VALUES (%s, %s, %s, %s)"
                                    params = (pseudo, mail, password, id_role)  # Vous devez définir id_role
                                    database.execute_sql(query, params)
            
                                    # Mettre à jour les variables de contrôle d'exécution de la page
                                    accueil.accueil_run = True
                                    self.page_inscription_run = False
                            else:
                                self.input_texts[self.active_input] += event.unicode
                                
                        
    def text_entry_register(self):
        self.solid_rect_radius(self.white, 320, 370, 220, 35)
        self.light_rect(self.black, 320, 370, 220, 35, 2)
        self.solid_rect_radius(self.white, 320, 445, 220, 35)
        self.light_rect(self.black, 320, 445, 220, 35, 2)
        
        self.text(16, self.input_texts['pseudo'], self.black, 225, 363)
        self.text(16, "*" * len(self.input_texts['password']), self.black, 225, 443)        
                        
    def home(self):
        while self.page_inscription_run:
            self.handle_events_for_register()
            
            self.Screen.fill(self.dark_grey)
            
            self.text_align(19, "Nom", self.white, 240, 335)
            self.text_align(19, "Prénom", self.white, 257, 410)
            self.text_align(19, "Pseudo", self.white, 240, 335)
            self.text_align(19, "Mot de passe", self.white, 287, 410)
            
            self.text_entry_register()
            
            self.solid_rect_radius(self.blue, 650, 430, 220, 35)
            self.text_align(21, "Inscription", self.black, 650, 430)
            
            self.text_entry_register()
            
            self.update()

        