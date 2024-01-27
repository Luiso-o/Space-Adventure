import pygame
import random
from objects.Player import Player
from objects.Bullet import Bullet
from objects.Explosion import Explosion
import resources.media as media

# Función principal del juego
def play():
    clock = pygame.time.Clock()

    #declarar variables y inicializarlas
    score = 0
    no_of_enemies = 15
    bullet = Bullet(0 , 480, 10, "ready", media.bulletimg)
    player = Player(370, 600, 4, media.playerimg)
    game_speed = 110
    game_collision = 0
    explosions = []
    enemyimg, enemyX, enemyY, enemyX_change, enemyY_change = game_configurations(no_of_enemies)
    in_game = True
    
    while in_game:
        clock.tick(game_speed)
        #Manejar eventos, actualizar y renderizar el juego
        media.screen.fill((0, 0, 0))
        # Limpiar la pantalla
        media.screen.blit(media.background, (0, 0))

        bullet = player.handle_events(bullet)

        current_time = pygame.time.get_ticks()
        explosions = [explosion for explosion in explosions if explosion.draw(current_time, media.screen)]
        
        # Bucle que se ejecuta para cada enemigo
        for i in range(no_of_enemies):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= 785:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]
                #if enemyY[i] >= 560:  
                    #game_over_text() 
                    #break 
                    
            # Comprobar si ha habido una colisión entre un enemigo y una bala
            if isCollision(enemyX[i], enemyY[i], bullet.x, bullet.y):
                bullet.y = 605 
                bullet.state = "ready"
                score += 1
                game_collision += 1
                
                explosions.append(Explosion(enemyX[i], enemyY[i], current_time))
                
                if game_collision == 20:
                    game_collision, game_speed = ingrease_speed(game_collision, game_speed)
                    
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 150)
            
            media.enemy(enemyX[i], enemyY[i], i, enemyimg)
              
        update_bullet(bullet)
        player.draw(media.screen)  
        media.show_score(score)
        pygame.display.update()

#actualizar bullet
def update_bullet(bullet):
    if bullet.y < 0:
        bullet.reset_position(454)
    if bullet.state == "fire":
        bullet.state = bullet.fire_bullet(bullet.x, bullet.y)
        bullet.y -= bullet.y_change

#funcion para aumentar la velocidad del juego
def ingrease_speed(game_collision, game_speed):
    game_speed += 15
    game_collision = 0
    return game_collision, game_speed

#funcion para comprobar si ha habido una colision entre la bala y el enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = (enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2
    return distance < 27 ** 2
                  
#Funcion que cunfigura las caracteristicas de los enemigos
def game_configurations(no_of_enemies):
    enemyimg = [random.choice([media.enemy1_img, media.enemy2_img, media.enemy3_img, media.enemy4_img]) for _ in range(no_of_enemies)]
    enemyX = [random.randint(0, 736) for _ in range(no_of_enemies)]
    enemyY = [random.randint(0, 150) for _ in range(no_of_enemies)]
    enemyX_change = [5 for _ in range(no_of_enemies)] 
    enemyY_change = [10 for _ in range(no_of_enemies)] 

    return enemyimg, enemyX, enemyY, enemyX_change, enemyY_change

#funcion para mostrar el texto de game over en pantalla
def game_over_text():
    screen_rect = media.screen.get_rect()
    over_text = media.over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=screen_rect.center)
    media.screen.blit(over_text, text_rect)