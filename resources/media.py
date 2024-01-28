import resources.put_media as put_media

# variables dimensiones del background y las naves
BACKGROUND_SIZE = (850, 700)
SPACESHIPS_SIZE = (60, 60)
GAME_OVER_FONT_SIZE = 60
SCORE_FONT_SIZE = 20

#Cargar icono de la ventana
icon_image = put_media.load_icon('assets/images/cohete.png')

#Cargar y redimensionar imagen de fondo
background = put_media.load_image('assets/images/background.jpg', BACKGROUND_SIZE)

#Establecer configuraciones de la pantalla
screen = put_media.setup_screen(BACKGROUND_SIZE)

#cargar y redimensionar la imagen del enemigos y jugador
enemy1_img = put_media.load_image('assets/images/enemy1.png', SPACESHIPS_SIZE)
enemy2_img = put_media.load_image('assets/images/enemy2.png',SPACESHIPS_SIZE)
enemy3_img = put_media.load_image('assets/images/enemy3.png',SPACESHIPS_SIZE)
enemy4_img = put_media.load_image('assets/images/enemy4.png',SPACESHIPS_SIZE)
playerimg = put_media.load_image('assets/images/space-invaders2.png', SPACESHIPS_SIZE)
  
#Cargar imagen de bala
bulletimg = put_media.load_image('assets/images/bullet4.png')

#Gargar imagen explosion al colisionar con un enemigo
explosion = put_media.load_image('assets/images/explosion.png', SPACESHIPS_SIZE)
  
#Cargar sonido de fondo
#background_sound = game_functions.load_background_sound('assets/audios/stay-retro.mp3')

#Cargar fuente para texto de game Over
over_font = put_media.load_font('assets/fonts/RAVIE.TTF', GAME_OVER_FONT_SIZE)

#Cargar fuente para texto de puntuar
font = put_media.load_font('assets/fonts/comicbd.ttf', SCORE_FONT_SIZE)

#funcion para mostrar la puntuacion en la pantalla
def show_score(score):
    score_value = font.render("SCORE " + str(score), True, (255,255,255))
    screen.blit(score_value, (10,10))
