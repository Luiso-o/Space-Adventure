import pygame
import sys
import random
import put_media

# variables dimensiones del background y las naves
BACKGROUND_SIZE = (850, 700)
SPACESHIPS_SIZE = (60, 60)
GAME_OVER_FONT_SIZE = 60
SCORE_FONT_SIZE = 20

#Cargar icono de la ventana
icon_image = put_media.load_icon('assets/assets/images/cohete.png')

#Cargar y redimensionar imagen de fondo
background = put_media.load_image('assets/assets/images/background.jpg', BACKGROUND_SIZE)

#Establecer configuraciones de la pantalla
screen = put_media.setup_screen(BACKGROUND_SIZE)

#cargar y redimensionar la imagen del enemigos y jugador
enemy1_img = put_media.load_image('assets/assets/images/enemy1.png', SPACESHIPS_SIZE)
enemy2_img = put_media.load_image('assets/assets/images/enemy2.png',SPACESHIPS_SIZE)
enemy3_img = put_media.load_image('assets/assets/images/enemy3.png',SPACESHIPS_SIZE)
enemy4_img = put_media.load_image('assets/assets/images/enemy4.png',SPACESHIPS_SIZE)
playerimg = put_media.load_image('assets/assets/images/space-invaders2.png', SPACESHIPS_SIZE)
  
#Cargar imagen de bala
bulletimg = put_media.load_image('assets/assets/images/bullet4.png')
  
#Cargar sonido de fondo
#background_sound = game_functions.load_background_sound('assets/assets/audios/stay-retro.mp3')

#Cargar fuente para texto de game Over
over_font = put_media.load_font('assets/assets/fonts/RAVIE.TTF', GAME_OVER_FONT_SIZE)

#Cargar fuente para texto de puntuar
font = put_media.load_font('assets/assets/fonts/comicbd.ttf', SCORE_FONT_SIZE)

#funcion para mostrar la puntuacion en la pantalla
def show_score(score):
    score_value = font.render("SCORE " + str(score), True, (255,255,255))
    screen.blit(score_value, (10,10))
        
#funcion para dibujar al enemigo en la pantalla
def enemy(x,y,i,enemyimg):
   screen.blit(enemyimg[i], (x,y))    

#funcion para comprobar si ha habido una colision entre la bala y el enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = (enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2
    return distance < 27 ** 2
   
#funcion para mostrar el texto de game over en pantalla
def game_over_text():
    screen_rect = screen.get_rect()
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=screen_rect.center)
    screen.blit(over_text, text_rect)

# Función para disparar la bala
def fire_bullet(x, y, bullet_state):
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))
    return bullet_state

#Metodo que controla el moviento del jugador y disparo
def handle_events(player, bullet_state, bulletX, bulletY):
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if keys_pressed[pygame.K_LEFT]:
        player.move_left()

    if keys_pressed[pygame.K_RIGHT]:
        player.move_right()

    if keys_pressed[pygame.K_SPACE]:
        if bullet_state == "ready":
            bulletX, bulletY = player.get_position()
            bullet_state = fire_bullet(bulletX, bulletY, bullet_state)

    if not keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_RIGHT]:
        player.stop_moving()

    return bulletX, bulletY, bullet_state