import pygame
from interface import Interface

# Créer une instance de la classe Interface
interface = Interface()

# Définir le contenu du texte à afficher
text_content = "TEXTE"
text_color = (249, 249, 249)
text_size = 30

# Obtenir les dimensions de la fenêtre
window_width, window_height = interface.get_size()

# Calculer les coordonnées pour centrer le texte
text_x = window_width // 2
text_y = window_height // 2

# Remplir l'écran avec la couleur de fond grise
interface.Screen.fill((54, 57, 63))

# Dessiner le texte au milieu de la fenêtre avec votre police
interface.text_align(text_size, text_content, text_color, text_x, text_y, interface.font())

# Mettre à jour et afficher la fenêtre
interface.update()

# Boucle principale du programme
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

