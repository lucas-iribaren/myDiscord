import pygame

class Interface:
    def __init__(self):
        self.W = 1000
        self.H = 600
        self.Screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Discord")
        self.clock_tick_refresh = pygame.time.Clock()                
        self.light_grey = (188, 186, 184)
        self.grey = (64, 68, 75)
        self.dark_grey = (54, 57, 63)
        self.white = (249, 249, 249)
        self.blue = (114, 137, 218)
        self.black = (0, 0, 0)
        self.red = (237, 32, 71)
        self.pur_red = (255, 0, 0)    
        self.dark_red = (120,11,11)    

    def img(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/images/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        self.Screen.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def img_background(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/image/{image_name}.png').convert()
        image = pygame.transform.scale(image, (largeur, hauteur))
        image.set_alpha(115)
        self.Screen.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def text(self, texte_size, texte_content, color, x, y):
        font = pygame.font.Font('files/font/helvetica_neue_regular.otf', texte_size)
        Texte = font.render(texte_content, True, color)
        Texte_rect = Texte.get_rect(topleft=(x, y))
        self.Screen.blit(Texte, Texte_rect)

    def text_align(self, texte_size, texte_content,color, x, y):
        font = pygame.font.Font('files/font/helvetica_neue_regular.otf', texte_size) 
        Texte = font.render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        self.Screen.blit(Texte, Texte_rect)

    def solid_rect(self,color, x, y, largeur, hauteur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x , y, largeur, hauteur))
    
    def solid_rect_radius(self, color, x, y, largeur,hauteur , radius):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y,largeur, hauteur),0,radius)   

    def light_rect(self, color, x, y, largeur, hauteur, epaisseur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y, largeur, hauteur),  epaisseur, 5)

    def light_rect1(self, color, x, y, largeur, hauteur, epaisseur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y, largeur, hauteur),  epaisseur, 100)
                
    def draw_overlay(self, coloralpha, x, y, largeur, hauteur):
        overlay_surface = pygame.Surface((largeur, hauteur), pygame.SRCALPHA)
        overlay_surface.fill(coloralpha)
        self.Screen.blit(overlay_surface, (x, y))
        
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
        
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock_tick_refresh.tick(60)  
        self.Screen.fill((0, 0, 0))
    
    def update_no_fill(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock_tick_refresh.tick(60)  

    def get_size(self):
        return self.Screen.get_size()

    def get_display(self):
        return self.Screen
    