import pygame
import random
import math
import sys
import os

#Inicializar pygame
pygame.init()

#obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# variables dimensiones del background y las naves
screen_width = 850
screen_height = 700
background_dimensions = (screen_width, screen_height)
spaceships_dimensions = (60,60)

#funcion para cargar y redimensionar imagenes
def load_and_resize_image(path, dimensions):
    return pygame.transform.scale(pygame.image.load(resource_path(path)), dimensions)

#establecer dimensiones de la pantalla
screen = pygame.display.set_mode((background_dimensions))

#Cargar icono de ventana
icon_image = resource_path('assets/assets/images/cohete.png')
icon = pygame.image.load(icon_image)

#Cargar y redimensionar imagen de fondo
background = load_and_resize_image('assets/assets/images/background.jpg', background_dimensions)

#Cargar sonido de fondo
background_sound = pygame.mixer.music.load(resource_path('assets/assets/audios/stay-retro.mp3'))

#Cargar imagen de jugador
playerimg = playerimg = load_and_resize_image('assets/assets/images/space-invaders2.png', spaceships_dimensions)

#Cargar imagen de bala
bulletimg = pygame.image.load(resource_path('assets/assets/images/bullet4.png'))

#Cargar fuente para texto de game Over
over_font = pygame.font.Font(resource_path('assets/assets/fonts/RAVIE.TTF'), 60)

#Cargar fuente para texto de puntuar
font = pygame.font.Font(resource_path('assets/assets/fonts/comicbd.ttf'), 20)

#Establecer titulo de ventana
pygame.display.set_caption("Space Adventure")

#Establecer icono de ventana
pygame.display.set_icon(icon)

#reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

#Crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

#Posicion inicial del jugador
playerX = 370
playerY = 600
playerx_change = 0
player_change = 0

#Lista para almacenar posiciones de los enemigos
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

#Iniciar las variables para guardar las posiciones de los enemigos
for i in range(no_of_enemies):
    #cargar la imagen del enemigo 1
    enemy1_img = load_and_resize_image('assets/assets/images/enemy3.png', spaceships_dimensions)
    enemyimg.append(enemy1_img)

    #cargar imagen de enemigo 2
    enemy2_img = load_and_resize_image('assets/assets/images/enemy4.png',spaceships_dimensions)
    enemyimg.append(enemy2_img)

    #Asignar una posicion aleatoria en X y Y para el enemigo
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))

    #Se establece la velocidad de movimiento del enemigo en X e Y
    enemyX_change.append(5)
    enemyY_change.append(10)

    #se inicializan las variables para guardar las posiciones en la tabla
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    #Se inicializa la puntuacion en 0
    score = 0

    #funcion para mostrar la puntuacion en la pantalla
    def show_score():
        score_value = font.render("SCORE " + str(score), True, (255,255,255))
        screen.blit(score_value, (10,10))

    #funcion para dibujar al jugador en la pantalla
    def player(x, y):
        screen.blit(playerimg, (x,y))

    #funcion para dibujar al enemigo en la pantalla
    def enemy(x,y,i):
        screen.blit(enemyimg[i], (x,y))

    #funcion para disparar la bala
    def fire_bullet(x,y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletimg, (x + 16, y +10))
    
    #funcion para comprobar si ha habido una colision entre la bala y el enemigo
    def isCollision(enemyX, enemyY, bulletX, bulletY):
      distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
      if distance < 27:
        return True
      else:
       return False
        
    #funcion para mostrar el texto de game over en pantalla
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255,255,255))
        text_rect = over_text.get_rect(
            center=(int(screen_width/2), int(screen_height/2)))
        screen.blit(over_text, text_rect)

    #funcion principal del juego
    def gameloop():

        #declara variables globales
        global score
        global playerX
        global playerx_change
        global bulletX
        global bulletY
        global collision
        global bullet_state

        in_game = True
        while in_game:
            #Maneja eventos, actualiza y renderiza el juego
            #Limpia la pantalla
            screen.fill((0,0,0))
            screen.blit(background, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    #Maneja el moviento del jugador y disparo
                    if event.key == pygame.K_LEFT:
                        playerx_change = -5

                    if event.key == pygame.K_RIGHT:
                        playerx_change = 5

                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)

                    if event.type == pygame.KEYUP:
                        playerx_change = 0
            
            #Aqui se esta actualizando la posicion del jugador
            playerX += playerx_change

            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736

            #Bucle que se ejecuta para cada enemigo
            for i in range(no_of_enemies):
                if enemyY[i] > 440:
                    for j in range(no_of_enemies):
                        enemyY[j] = 2000
                    game_over_text()

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 756:
                    enemyX_change[i] = -5
                    enemyY[i] += enemyY_change[i]

                #Aqui se comprueba si ha habido una colision entre un enemigo y una bala
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    bulletY = 454
                    bullet_state = "ready"
                    score += 1
                    enemyX[i] = random.randint(0,736)
                    enemyY[i] = random.randint(0,150)
                enemy(enemyX[i], enemyY[i], i)

            if bulletY < 0:
                bulletY = 454
                bullet_state = "ready"
            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change

            player(playerX,playerY)
            show_score()

            pygame.display.update()

            clock.tick(120)
        
gameloop()