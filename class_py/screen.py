import pygame

class Screen:
    def __init__(self):
        self.W = 1050
        self.H = 700
        self.fenetre = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Pokemon")
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.fenetre.fill((0, 0, 0))
    
    def update_no_fill(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)

    def get_size(self):
        return self.fenetre.get_size()

    def get_display(self):
        return self.fenetre
