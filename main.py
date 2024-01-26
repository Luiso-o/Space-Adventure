import pygame
import media,play_game

# Inicializar pygame
pygame.init()

# Establecer título de ventana
pygame.display.set_caption("Space Shooter")

# Reproducir sonido de fondo en loop
#pygame.mixer.music.play(-1)

# Inicializar la puntuación en 0
media.show_score(0)

play_game.play()
 