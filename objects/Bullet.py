import resources.media as media

class Bullet:
    def __init__(self, x, y, y_change, state, image):
        self._x = x
        self._y = y
        self._y_change = y_change
        self._state = state
        self._image = image

    # Getter y setter para la propiedad x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # Getter y setter para la propiedad y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # Getter y setter para la propiedad y_change
    @property
    def y_change(self):
        return self._y_change

    @y_change.setter
    def y_change(self, value):
        self._y_change = value

    # Getter y setter para la propiedad state
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        
    # Función para disparar la bala
    def fire_bullet(self, x, y):
        self.state = "fire"
        media.screen.blit(self._image, (x + 16, y + 10))
        return self.state
    
    def reset_position(self, y):
        self.y = y
        self.state = "ready"
