import pygame
import random
from objects.Player import Player
from objects.Bullet import Bullet
import media

# Función principal del juego
def play():
    clock = pygame.time.Clock()

    #declarar variables y inicializarlas
    score = 0
    no_of_enemies = 15
    bullet = Bullet(0 , 480, 10, "ready")
    player = Player(370, 600, 4, media.playerimg)
    enemyimg, enemyX, enemyY, enemyX_change, enemyY_change = game_configurations(no_of_enemies)
    in_game = True
    
    while in_game:
        clock.tick(110)
        #Manejar eventos, actualizar y renderizar el juego
        media.screen.fill((0, 0, 0))
        # Limpiar la pantalla
        media.screen.blit(media.background, (0, 0))

        bullet.x, bullet.y, bullet.state = media.handle_events(player, bullet.state, bullet.x, bullet.y)

        # Bucle que se ejecuta para cada enemigo
        for i in range(no_of_enemies):
            if enemyY[i] > player.get_y():
                for j in range(no_of_enemies):
                    enemyY[j] = 650
                media.game_over_text()

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 785:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]
            
            # Comprobar si ha habido una colisión entre un enemigo y una bala
            collision = media.isCollision(enemyX[i], enemyY[i], bullet.x, bullet.y)
            if collision:
                bullet.y = 454
                bullet.state = "ready"
                score += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 150)
            media.enemy(enemyX[i], enemyY[i], i, enemyimg)

        if bullet.y < 0:
            bullet.y = 454
            bullet.state = "ready"
        if bullet.state == "fire":
            bullet.state = media.fire_bullet(bullet.x, bullet.y, bullet.state)
            bullet.y -= bullet.y_change

        player.draw(media.screen)  

        media.show_score(score)

        pygame.display.update()
        
       

        
        
#Funcion que cunfigura las caracteristicas de los enemigos
def game_configurations(no_of_enemies):
    enemyimg = [random.choice([media.enemy1_img, media.enemy2_img, media.enemy3_img, media.enemy4_img]) for _ in range(no_of_enemies)]
    enemyX = [random.randint(0, 736) for _ in range(no_of_enemies)]
    enemyY = [random.randint(0, 150) for _ in range(no_of_enemies)]
    enemyX_change = [5 for _ in range(no_of_enemies)] 
    enemyY_change = [10 for _ in range(no_of_enemies)] 

    return enemyimg, enemyX, enemyY, enemyX_change, enemyY_change