import pygame
import random
from objects.Player import Player
from objects.Bullet import Bullet
from objects.Explosion import Explosion
from objects.Enemy import Enemy
import resources.media as media

# Función principal del juego
def play():
    clock = game_init()

    #declarar variables y inicializarlas
    score = 0
    number_of_enemies = 15
    game_speed = 110
    game_collision = 0
    explosions = []
    in_game = True
    game_over = False
    
    #Instaciar las clases 
    bullet = Bullet(0 , 480, 10, "ready", media.bulletimg)
    player = Player(370, 600, 4, media.playerimg)
    enemies = game_configurations(number_of_enemies)
    
    while in_game:
        clock.tick(game_speed)
        
        media.screen.fill((0, 0, 0))
        media.screen.blit(media.background, (0, 0))

        bullet = player.handle_events(bullet)

        current_time = pygame.time.get_ticks()
        explosions = [explosion for explosion in explosions if explosion.draw(current_time, media.screen)]
        
        # Bucle que se ejecuta para cada enemigo
        for enemy in enemies:
            enemy.move()
            enemy.draw(media.screen)
            
            if enemy.y >= 550:
                game_over = True
                break
                    
            # Comprobar si ha habido una colisión entre un enemigo y una bala
            if isCollision(enemy.x, enemy.y, bullet.x, bullet.y):
                bullet.y = 600
                bullet.state = "ready"
                score += 1
                game_collision += 1
                
                explosions.append(Explosion(enemy.x, enemy.y, current_time))
                
                if game_collision == 20 and game_speed <= 200 :
                    game_collision, game_speed = ingrease_speed(game_collision, game_speed)
                    
                enemy.x = random.randint(0, 736)
                enemy.y = random.randint(0, 150)
        
        if game_over:
            restart = game_over_text()
            if restart:
                return play()
            else: 
                break
                         
        update_bullet(bullet)
        player.draw(media.screen)  
        media.show_score(score)
        pygame.display.update()
        

#inicializar pygame y las configuraciones iniciales del juego      
def game_init():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space Shooter")
    #pygame.mixer.music.play(-1)  
    media.show_score(0)
    return clock

#actualizar bullet
def update_bullet(bullet):
    if bullet.y < 0:
        bullet.reset_position(454)
    if bullet.state == "fire":
        bullet.state = bullet.fire_bullet(bullet.x, bullet.y)
        bullet.y -= bullet.y_change

#funcion para aumentar la velocidad del juego
def ingrease_speed(game_collision, game_speed):
    game_speed += 10
    game_collision = 0
    return game_collision, game_speed

#funcion para comprobar si ha habido una colision entre la bala y el enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = (enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2
    return distance < 27 ** 2
                  
#Funcion que cunfigura las caracteristicas de los enemigos
def game_configurations(number_of_enemies):
    return [Enemy(random.randint(0, 736), random.randint(50, 150)) for _ in range(number_of_enemies)]

#Se escriben los textos game over, se reinicia o se cierra el juego
def game_over_text():
    screen_rect = media.screen.get_rect()
    over_text = media.over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=(screen_rect.centerx, screen_rect.centery - 50))
    media.screen.blit(over_text, text_rect)

    small_font = pygame.font.Font(None, 40) 

    enter_text = small_font.render("Restart: Enter", True, (0, 255, 0))
    enter_text_rect = enter_text.get_rect(center=(screen_rect.centerx, screen_rect.centery + 20))
    media.screen.blit(enter_text, enter_text_rect)

    escape_text = small_font.render("Close: Esc", True, (255, 0, 0))
    escape_text_rect = escape_text.get_rect(center=(screen_rect.centerx, screen_rect.centery + 50))
    media.screen.blit(escape_text, escape_text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False