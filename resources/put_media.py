import pygame
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

#funcion para cargar y redimensionar imagenes
def load_image(path, size=None):
    try:
        if size:
            return pygame.transform.scale(pygame.image.load(resource_path(path)), size)
        else:
            return pygame.image.load(resource_path(path))
    except pygame.error as e:
        print(f"Error al cargar la imagen: {path}")
        print(e)
        return None
    
#funcion para cargar el icono de la aplicacion
def load_icon(path):
    try:
        icon_image = pygame.image.load(resource_path(path))
        pygame.display.set_icon(icon_image)
    except pygame.error as e:
        print(f"Error al cargar el icono de juego: {path}")
        print(e)
        return None

#funcion para cargar y redimensionar sonido
def load_background_sound(path):
    try:
        pygame.mixer.music.load(resource_path(path))
    except pygame.error as e:
        print(f"Error al cargar el sonido de fondo: {path}")
        print(e)
        return None
 
#funcion para cargar y redimensionar fuentes
def load_font(path, size):
    try:
        return pygame.font.Font(resource_path(path), size)
    except pygame.error as e:
        print(f"Error al cargar la fuente: {path}")
        print(e)
        return None

#funcion para redimensionar el tamano de la pantalla
def setup_screen(size):
    try:
        screen = pygame.display.set_mode(size)
        return screen
    except pygame.error as e:
        print(f"Error al configurar la pantalla: {e}")
        return None
    