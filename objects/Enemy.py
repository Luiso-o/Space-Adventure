import random
import resources.media as media

class Enemy:
    def __init__(self, x, y):
        self.image = random.choice([media.enemy1_img, media.enemy2_img, media.enemy3_img, media.enemy4_img])
        self.x = x
        self.y = y
        self.x_change = 5
        self.y_change = 10

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= 736:  
            self.x_change *= -1
            self.y += self.y_change

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
