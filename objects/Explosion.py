import resources.media as media

class Explosion:
    def __init__(self, x, y, start_time):
        self.x = x
        self.y = y
        self.start_time = start_time
        self.duration = 30  

    def draw(self, current_time, screen):
        if current_time - self.start_time < self.duration:
            screen.blit(media.explosion, (self.x, self.y))
        else:
            return False  
        return True
