import pygame
import resources.media as media,play_game

pygame.init()
pygame.display.set_caption("Space Shooter")
#pygame.mixer.music.play(-1)  
media.show_score(0)

play_game.play() 