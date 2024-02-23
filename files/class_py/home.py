import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.profile import Profile
from files.class_py.register import Register
# from files.class_py.notification import Notification

class Home(Interface):
    def __init__(self):
        """
        Initialize the Home class.
        """
        Interface.__init__(self)
        self.database = Database()
        self.input_texts = {'username':'', 'password': ''}
        self.active_input = None
        self.error_message_login = ""
        self.home_Home = True
        self.clicked_rect = None
        self.clicked_input = None
        self.clock = pygame.time.Clock()
        self.page_register = Register()
        self.error_timer = 0
        self.error_duration = 1000

  
    def handle_events_for_login(self):
        """
        Handle events for login.
        """
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
                        self.active_input = 'password' if self.active_input == 'username' else 'username'
                    elif event.key == pygame.K_RETURN:
                        if (self.input_texts['username'] != '' and
                            self.input_texts['password'] != ''):
                                self.button_login()
                        else:
                            self.error_message_login = "Error, invalid username or password. Please try again"
                    else:
                        self.input_texts[self.active_input] += event.unicode
                    
                            
            # Event mouse          
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.is_mouse_over_button(pygame.Rect( 210, 488, 220, 35)):
                        if (self.input_texts['username'] != '' and
                            self.input_texts['password'] != ''):
                                self.button_login()
                        else:
                            self.error_message_login = "Error, invalid username or password. Please try again"
                    elif self.is_mouse_over_button(pygame.Rect(535, 420, 220, 35)):
                        self.page_register.register_run = True
                        self.page_register.register()
                    
                    else:
                        # Verify if the mouse is clicked on the input rect 
                        for input_rect in [(210, 345, 220, 35), (210, 420, 220, 35)]:
                            if self.is_mouse_over_button(pygame.Rect(input_rect)):
                                # Keep track of the previously clicked rectangle and activate text input
                                self.clicked_rect = input_rect
                                self.active_input = 'username' if input_rect == (210, 345, 220, 35) else 'password'                                 
                     

    def text_entry_login(self):        
        """
        Display text entry for login.
        """
        self.text(16, self.input_texts['username'], self.black, 220, 352)
        self.text(16, "*" * len(self.input_texts['password']), self.black, 220, 433)
        
        if self.clicked_input:
            self.text(16, self.input_texts[self.clicked_input], self.black, self.clicked_rect[0] + 10, self.clicked_rect[1] + 7)

    def mouse_effects(self):
        """
        Apply mouse effects.
        """
        if self.is_mouse_over_button(pygame.Rect(210,345,220,35)): # User text field
            self.light_rect(self.black, 210, 345, 220, 35, 1)
        
        if self.is_mouse_over_button(pygame.Rect(210,420,220,35)): # Password text field
            self.light_rect(self.black, 210, 420, 220, 35, 1)

        if self.is_mouse_over_button(pygame.Rect(210, 488, 220, 35)): # Login button
            self.light_rect(self.black, 210, 488, 220, 35, 1)
        
        if self.is_mouse_over_button(pygame.Rect(535, 420, 220, 35)): # Register button
            self.light_rect(self.black, 535, 420, 220, 35, 1)

    def verify_account_exist(self, username_entry, password_entry):
        """
        Verify if account exists.
        """
        # Check if entries are not empty
        if username_entry and password_entry:
            sql = "SELECT pseudo, password FROM user WHERE pseudo = %s;"
            self.user_data = self.database.fetch_one(sql, (username_entry,))
            if self.user_data:
                self.username_user = self.user_data[0]
                if self.user_data[1] == password_entry:
                     return True                   
                else:                   
                    self.error_message_login = "Error, incorrect password"
                    return False
            else:
                self.error_message_login = "Error, incorrect username"
                return False
        else:
            self.error_message_login = "Error, please enter a username and password"
            return False, None
      
    def draw_error_message_login(self):
        """
        Draw error message for login.
        """
        if self.error_message_login:
            self.solid_rect_radius(self.light_grey,620,20,360,55,8)
            self.light_rect(self.black,620,20,360,55,2)
            self.text_align(16, self.error_message_login, self.pur_red, 796, 45)
            self.error_timer += self.clock.tick()
            if self.error_timer >= self.error_duration:
                self.error_message_login = None
                self.error_timer = 0
                                    
    def button_login(self):
        """
        Handle login button click.
        """
        if self.verify_account_exist(self.input_texts['username'], self.input_texts['password']):
            self.page_profil = Profile(self.username_user)
            # self.notif = Notification()
            self.page_profil.home_profile()
            self.Home_run = False                      
                     
        
    def home(self):
        """
        Run the home interface.
        """
        self.Home_run = True
        self.active_input = 'username'  
        
        while self.Home_run:
            
            if self.home_Home:
                self.handle_events_for_login()

                self.Screen.fill(self.dark_grey)

                self.img(330, 160, 230, 220, "icones/logo")
                self.text_align(70, "MyDiscord", self.white, 610, 160)
                
                self.light_rect(self.light_grey, 160, 300, 670, 270, 5)
                # User text field  
                self.text_align(19, "Nom d'utilisateur", self.white, 268, 330) # Text 
                self.solid_rect_radius(self.white, 210, 345, 220, 35,8)# Block

                # Password text field
                self.text_align(19, "Mot de passe", self.white, 257, 405)# Text 
                self.solid_rect_radius(self.white, 210, 420, 220, 35,8)# Block
                
                # Login button
                self.solid_rect_radius(self.blue, 210, 488, 220, 35, 8)# Block 
                self.text_align(21, "Connexion", self.black, 315, 505)# Text

                self.text_align(21, "Ou", self.white, 485, 435)# Text
                
                self.solid_rect_radius(self.blue, 535, 420, 220, 35, 8)# Register button
                self.text_align(21, "Inscription", self.black, 642, 436)# Text

                self.text_entry_login() 
                self.draw_error_message_login() # Notification error
                self.mouse_effects() # Mouse hover effects
                self.update()
