import pygame

class Interface:
    def __init__(self):
        self.W = 1000
        self.H = 600
        self.Screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Discord")
        self.clock = pygame.time.Clock()
        self.light_grey = (188, 186, 184)
        self.grey = (64, 68, 75)
        self.dark_grey = (54, 57, 63)
        self.white = (249, 249, 249)
        self.blue = (114, 137, 218)
        self.black = (0, 0, 0)
        self.red = (237, 32, 71)
        self.pur_red = (255, 0, 0)    
        self.dark_red = (120,11,11)    
        self.soft_black = (35,35,35)
        self.purple = (185, 12, 211)
    def img(self, x, y, width, height, image_name):
        image = pygame.image.load(f'images/{image_name}.png')
        image = pygame.transform.scale(image, (width, height))
        self.Screen.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def img_background(self, x, y, width, height, image_name):
        image = pygame.image.load(f'images/{image_name}.png').convert()
        image = pygame.transform.scale(image, (width, height))
        image.set_alpha(115)
        self.Screen.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def text(self, text_size, text_content, color, x, y):
        font = pygame.font.Font('font/helvetica_neue_regular.otf', text_size)
        text = font.render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Screen.blit(text, text_rect)
        
    def text_jump_line(self, text_size, text_content, color, x, y, line_spacing=15, max_height=600):
        font = pygame.font.Font('font/helvetica_neue_regular.otf', text_size)
        lines = text_content.split('\n')
        y_offset = 0
        total_height = 0  # Initialize the total height of lines
        for line in lines:
            text_surface = font.render(line, True, color)
            total_height += text_surface.get_height() + line_spacing  # Update the total height
            if total_height > max_height:  # Check if total height exceeds the limit
                # Move to the next line by adjusting the Y position
                y += total_height - max_height
                total_height = text_surface.get_height() + line_spacing
            text_rect = text_surface.get_rect(topleft=(x, y + y_offset))
            self.Screen.fill(self.grey, text_rect)
            self.Screen.blit(text_surface, text_rect)
            y_offset += text_surface.get_height() + line_spacing


    def text_align(self, text_size, text_content,color, x, y):
        font = pygame.font.Font('font/helvetica_neue_regular.otf', text_size) 
        text = font.render(text_content, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.Screen.blit(text, text_rect)

    def solid_rect(self,color, x, y, width, height):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x , y, width, height))
    
    def solid_rect_radius(self, color, x, y, width,height , radius):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y,width, height),0,radius)   

    def light_rect(self, color, x, y, width, height, epaisseur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y, width, height),  epaisseur, 5)

    def light_rect_radius(self, color, x, y, width, height, epaisseur, radius):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y, width, height),  epaisseur, radius)
                
    def draw_overlay(self, coloralpha, x, y, width, height):
        overlay_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay_surface.fill(coloralpha)
        self.Screen.blit(overlay_surface, (x, y))
        
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
    
    