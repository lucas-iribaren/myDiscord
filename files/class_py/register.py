import pygame, re
from files.class_py.user import User
from files.class_py.interface import Interface

class Register(Interface, User):
    def __init__(self):
        Interface.__init__(self)
        User.__init__(self)
        self.register_page = True
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

    def add_users(self):
        if (self.input_texts['email'] != '' and self.input_texts['pseudo'] != '' and self.input_texts['password'] != ''):
            if self.is_valid_email(self.input_texts['email']):
                self.add_user(self.input_texts['pseudo'], self.input_texts['email'], self.input_texts['password'], 1)
                self.error_message_register = "Votre compte à bien été ajouté !"
            else:
                self.error_message_register = "Erreur, l'adresse mail n'est pas valide."
        else:
            self.error_message_register = "Erreur, vous devez remplir toute les cases pour l'inscription."

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
                        elif self.active_input == 'password':
                            self.active_input = 'email'
                    elif event.key == pygame.K_RETURN:
                        self.add_users()
                    else:
                        self.input_texts[self.active_input] += event.unicode
                            
            # Event mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.is_mouse_over_button(pygame.Rect(420,420,220,35)): #Button 'register'
                        self.add_users()
                    elif self.is_mouse_over_button(pygame.Rect(370,520,280,20)): #Button 'Vous avez déjà un compte?'
                        self.register_run = False
                    else:
                        # Verify if the mouse is clicked on the input rect
                        for input_rect in [(390,170,280,30), (390, 250, 280, 30), (390, 330, 280, 30)]:
                            if self.is_mouse_over_button(pygame.Rect(input_rect)):
                                # Save the rect clicked and active input text  
                                self.clicked_rect = input_rect
                                self.active_input = 'email' if input_rect == (390, 170, 280, 30) else ('pseudo' if input_rect == (390, 250, 280, 30) else 'password')
                     
    def draw_error_message_register(self):
        if self.error_message_register:
            self.solid_rect_radius(self.light_grey,620,20,360,55,8)
            self.text_align(16, self.error_message_register, self.pur_red, 796, 45)
            self.light_rect(self.black,620,20,360,55,2)
            self.error_timer += self.clock.tick()
            if self.error_timer >= self.error_duration:
                self.error_message_register = None
                self.error_timer = 0

    def mouse_effets(self):
        if self.is_mouse_over_button(pygame.Rect(390,170,280,30)):# input text area email
            self.light_rect(self.black,390,170,280,30,1)

        if self.is_mouse_over_button(pygame.Rect(390,250,280,30)):# input text area pseudo
            self.light_rect(self.black,390,250,280,30,1)

        if self.is_mouse_over_button(pygame.Rect(390,330,280,30)):# input text area password
            self.light_rect(self.black,390,330,280,30,1)

        if self.is_mouse_over_button(pygame.Rect(420,420,220,35)):# Button register
            self.light_rect(self.black,420,420,220,35,1)
            
    def register(self):
        while self.register_run:
            if self.register_page:
                self.event_type()
                self.Screen.fill(self.dark_grey)# background
                self.solid_rect_radius(self.grey,350,50,350,500,8)# block register
                self.solid_rect_radius(self.light_grey,460,55,150,50,8)# border
                self.text(20,'Créer votre compte',self.black,470,68)                
                self.solid_rect_radius(self.blue,420,420,220,35,8)
                self.text_align(21,"S'inscrire",self.black,530,436)

                # Block Email
                self.solid_rect_radius(self.light_grey,390,170,280,30,5)#Block email
                self.text(19,"Email",self.white,390,140)

                # Block Pseudo
                self.solid_rect_radius(self.light_grey, 390, 250, 280, 30, 5)#Block pseudo
                self.text(19,"Nom d'utilisateur",self.white,390,220)

                # Block Password
                self.solid_rect_radius(self.light_grey, 390, 330, 280, 30, 5)#Block password
                self.text(19,"Mot de passe",self.white,390,300)
                
                # Return home
                if self.is_mouse_over_button(pygame.Rect(370,520,280,20)):
                    self.text_align(18,"Tu as déjà un compte?",self.black,435,520)
                else:
                    self.text_align(15,"Tu as déjà un compte?",self.black,435,520)
                    
                self.draw_error_message_register()
                self.mouse_effets()
                self.select_input()
                
                        
                self.update()

    def select_input(self):
        self.text(16, self.input_texts['email'], self.black, 400, 175)
        self.text(16, self.input_texts['pseudo'], self.black, 400, 255)
        self.text(16, self.input_texts['password'], self.black, 400, 335)
        if self.selected_rect:
            self.text(16, self.input_texts[self.selected_rect], self.black, self.clicked_rect[0] + 10, self.clicked_rect[1] + 7)