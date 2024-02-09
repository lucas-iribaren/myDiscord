import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.page_profil import PageProfil
page_profil = PageProfil()

class Accueil(Interface):
    def __init__(self):
        Interface.__init__(self)
        self.database = Database()
        self.input_texts = {'nom_utilisateur': 'azerty', 'password': ''}  
        self.active_input = None
        self.error_message = ""
        self.home_accueil = True 
        self.surface = pygame.display.set_mode((self.W,self.H))
  
# Initialing Color
        self.color = (255,0,0)
  
    def handle_events_for_login(self):
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
                        self.active_input = 'password' if self.active_input == 'nom_utilisateur' else 'nom_utilisateur'
                    else:
                        self.input_texts[self.active_input] += event.unicode
                            
            # Event mouse          
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.is_mouse_over_button(pygame.Rect(320, 505, 220, 35)):
                        print('click')
                        if (self.input_texts['nom_utilisateur'] != '' and
                            self.input_texts['password'] != ''):
                                self.button_login()
                        else:
                            self.error_message = "Erreur, identifiant ou mot de passe invalide. Veuillez ressayer"             
                     

    def text_entry_login(self):
        self.solid_rect_radius(self.white, 210, 345, 220, 35,8)
        self.light_rect(self.black, 210, 345, 220, 35, 2)
        self.solid_rect_radius(self.white, 210, 420, 220, 35,8)
        self.light_rect(self.black, 210, 420, 220, 35, 2)
        
        self.text(16, self.input_texts['nom_utilisateur'], self.black, 220, 352)
        self.text(16, "*" * len(self.input_texts['password']), self.black, 220, 433)
        
        
    def verify_account_exist(self, nom_utilisateur_entry, password_entry):
        # Vérifier si les entrées ne sont pas vides
        if nom_utilisateur_entry and password_entry:
            # Récupérer les informations de l'utilisateur à partir de la base de données
            user_data = self.database.fetch_one("SELECT nom_utilisateur, password FROM user WHERE nom_utilisateur = ?;", (nom_utilisateur_entry,))
            if user_data:
                # Si l'utilisateur est trouvé dans la base de données, vérifier le mot de passe
                if user_data[1] == password_entry:
                    return True  # Si le mot de passe correspond, retourner True
        return False  # Si aucune correspondance n'est trouvée, retourner False
    
    
    def draw_error_message(self):
        if self.error_message:
            # Afficher le message d'erreur en rouge
            self.text_align(18, self.error_message, (255, 0, 0), 500, 550)  # Vous pouvez ajuster la position et la taille du message
    
    def button_login(self):
        if self.verify_account_exist(self.input_texts['nom_utilisateur'], self.input_texts['password']):
            page_profil.home_profil()
            self.accueil_run = False            
        else:
           self.draw_error_message()             
        
    def home(self):
        self.accueil_run = True
        self.active_input = 'nom_utilisateur'  
        
        while self.accueil_run:
            
            if self.home_accueil:
                self.handle_events_for_login()

# Drawing Rectangle
                self.Screen.fill(self.dark_grey)

                self.img(330, 160, 230, 220, "icones/logo")
                self.text_align(70, "MyDiscord", self.white, 610, 160)
                
                self.text_align(19, "Nom d'utilisateur", self.white, 268, 330)
                self.text_align(19, "Mot de passe", self.white, 257, 405)
                self.light_rect(self.light_grey, 160, 300, 670, 270, 5)
                
                self.text_entry_login()  # Appeler la fonction pour gérer la saisie de texte
                
                self.solid_rect_radius(self.blue, 210, 488, 220, 35, 8)
                self.text_align(21, "Connexion", self.black, 315, 505)
                self.text_align(21, "Ou", self.white, 485, 435)
                
                self.solid_rect_radius(self.blue, 535, 420, 220, 35,8)
                self.text_align(21, "Inscription", self.black, 642, 436)
                if self.is_mouse_over_button(pygame.Rect(320, 505, 220, 35)):
                    pygame.draw.rect(self.surface, self.color, pygame.Rect(320, 505, 220, 35),  1)      
                
                self.draw_error_message()

                self.update()
               
