import pygame

class Interface:
    def __init__(self):
        self.W = 1000
        self.H = 600
        self.Screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Discord")
        self.clock = pygame.time.Clock()    

    def font(self):
        return pygame.font.Font("files/font/helvetica_neue_regular.otf",80)

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

    def text_align(self, texte_size, texte_content,color, x, y, font):
        Texte = font.render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        self.Screen.blit(Texte, Texte_rect)

    def solid_rect(self, color, x, y, largeur, longueur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur))
    
    def solid_rect_radius(self, color, x, y, longueur, largeur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x - longueur//2, y - largeur//2, longueur, largeur),  0, 8)   

    def light_rect(self, color, x, y, largeur, longueur, epaisseur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, 5)

    def light_rect1(self, color, x, y, largeur, longueur, epaisseur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, 100)
                
    def draw_overlay(self, coloralpha, x, y, largeur, longueur):
        overlay_surface = pygame.Surface((largeur, longueur), pygame.SRCALPHA)
        overlay_surface.fill(coloralpha)
        self.Screen.blit(overlay_surface, (x - largeur // 2, y - longueur // 2))
        
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
        
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.Screen.fill((0, 0, 0))
    
    def update_no_fill(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)

    def get_size(self):
        return self.Screen.get_size()

    def get_display(self):
        return self.Screen
    