import pygame

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
