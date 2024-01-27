import pygame
import sys

class Player:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_speed(self):
        return self.speed
    
    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def stop_moving(self):
        pass

    def get_position(self):
        return self.x, self.y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
       
    # Metodo que controla el movimiento del jugador y disparo
    def handle_events(self, bullet):
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if keys_pressed[pygame.K_LEFT]:
            self.move_left()

        if keys_pressed[pygame.K_RIGHT]:
            self.move_right()

        if keys_pressed[pygame.K_SPACE]:
            if bullet.state == "ready":
                bullet.x, bullet.y = self.get_position()
                bullet.fire_bullet(bullet.x, bullet.y)

        if not keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_RIGHT]:
            self.stop_moving()

        return bullet
