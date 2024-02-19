import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.profil import Profil
from files.class_py.inscription import Inscription

class Accueil(Interface):
    def __init__(self):
        Interface.__init__(self)
        self.database = Database()
        self.input_texts = {'nom_utilisateur':'', 'password': ''}  
        self.active_input = None
        self.error_message_login = ""
        self.home_accueil = True
        self.clicked_rect = None  
        self.clicked_input = None
        self.clock = pygame.time.Clock()        
        self.page_register = Inscription()
        self.error_timer = 0
        self.error_duration = 3500
        
  
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
                    elif event.key == pygame.K_RETURN:
                        if (self.input_texts['nom_utilisateur'] != '' and
                            self.input_texts['password'] != ''):
                                self.button_login()
                        else:
                            self.error_message_login = "Erreur, identifiant ou mot de passe invalide. Veuillez ressayer"
                    else:
                        self.input_texts[self.active_input] += event.unicode
                    
                            
            # Event mouse          
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.is_mouse_over_button(pygame.Rect( 210, 488, 220, 35)):
                        print('click')
                        if (self.input_texts['nom_utilisateur'] != '' and
                            self.input_texts['password'] != ''):
                                self.button_login()
                        else:
                            self.error_message_login = "Erreur, identifiant ou mot de passe invalide. Veuillez ressayer"
                    elif self.is_mouse_over_button(pygame.Rect(535, 420, 220, 35)):
                        self.page_register.register_run = True
                        self.page_register.register()
                    
                    else:
                        # Vérifier si le clic est sur l'un des rectangles d'entrée de texte
                        for input_rect in [(210, 345, 220, 35), (210, 420, 220, 35)]:
                            if self.is_mouse_over_button(pygame.Rect(input_rect)):
                                # Garder en mémoire le rectangle cliqué précédemment et activer l'entrée de texte
                                self.clicked_rect = input_rect
                                self.active_input = 'nom_utilisateur' if input_rect == (210, 345, 220, 35) else 'password'                                 
                     

    def text_entry_login(self):        
        self.text(16, self.input_texts['nom_utilisateur'], self.black, 220, 352)
        self.text(16, "*" * len(self.input_texts['password']), self.black, 220, 433)
        
        if self.clicked_input:
            self.text(16, self.input_texts[self.clicked_input], self.black, self.clicked_rect[0] + 10, self.clicked_rect[1] + 7)

    def mouse_effects(self):
        if self.is_mouse_over_button(pygame.Rect(210,345,220,35)): # Champ texte user
            self.light_rect(self.black, 210, 345, 220, 35, 1)
        
        if self.is_mouse_over_button(pygame.Rect(210,420,220,35)): # Champ texte MDP
            self.light_rect(self.black, 210, 420, 220, 35, 1)

        if self.is_mouse_over_button(pygame.Rect(210, 488, 220, 35)): #Bouton connexion
            self.light_rect(self.black, 210, 488, 220, 35, 1)
        
        if self.is_mouse_over_button(pygame.Rect(535, 420, 220, 35)): #Bouton inscription
            self.light_rect(self.black, 535, 420, 220, 35, 1)

    def verify_account_exist(self, nom_utilisateur_entry, password_entry):
        # Vérifier si les entrées ne sont pas vides
        if nom_utilisateur_entry and password_entry:
            sql = "SELECT pseudo, password FROM user WHERE pseudo = %s;"
            self.user_data = self.database.fetch_one(sql, (nom_utilisateur_entry,))
            if self.user_data:
                if self.user_data[1] == password_entry:
                     return True                   
                else:                   
                    self.error_message_login = "Erreur, le mot de passe n'est pas correct"
                    return False
            else:
                self.error_message_login = "Erreur, nom d'utilisateur incorrect"
                return False
        else:
            self.error_message_login = "Erreur, veuillez saisir un nom d'utilisateur et un mot de passe"
            return False
      
    def draw_error_message_login(self):
        if self.error_message_login:
            self.solid_rect_radius(self.light_grey,620,20,360,55,8)
            self.light_rect(self.black,620,20,360,55,2)
            self.text_align(16, self.error_message_login, self.pur_red, 796, 45)
            self.error_timer += self.clock.tick()
            if self.error_timer >= self.error_duration:
                self.error_message_login = None
                self.error_timer = 0
                                    
    def button_login(self):
        if self.verify_account_exist(self.input_texts['nom_utilisateur'], self.input_texts['password']):
            self.page_profil = Profil(self.user_data)
            self.page_profil.home_profil()
            self.accueil_run = False                   
                      
    def home(self):
        self.accueil_run = True
        self.active_input = 'nom_utilisateur'  
        
        while self.accueil_run:
            
            if self.home_accueil:
                self.handle_events_for_login()

                self.Screen.fill(self.dark_grey)

                self.img(330, 160, 230, 220, "icones/logo")
                self.text_align(70, "MyDiscord", self.white, 610, 160)
                
                self.light_rect(self.light_grey, 160, 300, 670, 270, 5)
                # Champ de texte Utilisateur  
                self.text_align(19, "Nom d'utilisateur", self.white, 268, 330) # Texte 
                self.solid_rect_radius(self.white, 210, 345, 220, 35,8)# Bloc

                # Champ de texte Mot de Passe
                self.text_align(19, "Mot de passe", self.white, 257, 405)# Texte 
                self.solid_rect_radius(self.white, 210, 420, 220, 35,8)# Bloc
                
                # Bloc connexion
                self.solid_rect_radius(self.blue, 210, 488, 220, 35, 8)# Bloc 
                self.text_align(21, "Connexion", self.black, 315, 505)# Texte

                self.text_align(21, "Ou", self.white, 485, 435)# Texte
                
                self.solid_rect_radius(self.blue, 535, 420, 220, 35, 8)# Bloc Inscription
                self.text_align(21, "Inscription", self.black, 642, 436)# Texte

                self.text_entry_login() 
                self.draw_error_message_login() #Notification error
                self.mouse_effects() # Surlignement souris
                self.update()
               
