# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
import math


class Hunter(Pulsator,Mobile_Simulton):
    speed = 5
    vision = 200
    color = 'black'
    radius = 10
    
    def __init__(self, x, y, width, height, speed, angle, color):
        
        Pulsator.__init__(self, x, y, width, height, color)
        Mobile_Simulton.__init__(self, x, y, width, height, angle, speed)
        
        self._x = x
        self._y = y
        self._width = width * 2
        self._height = height * 2
        self._speed = speed
        self._angle = angle
        self._color = color
        self._close_items = []
        self._smallest = 0
        self.obj_eaten = set()
        
        self.randomize_angle()
    
    
    def update(self, model):
        
        # If our counter reaches 30, decrease size and reset counter.
        if self.temp_counter == self.counter:
            self._width -= 1
            self._height -= 1
            self.temp_counter = 0
            self.set_dimension(self._width, self._height)
        
        # If our width or height reaches 0, return Dead
        if self._width == 0 or self._height == 0:
            return 'Dead'
        
        # If hunter doesn't eat, add 1 to the counter.
        if len(self.obj_eaten) == self.eaten_counter:
            self.temp_counter += 1
            
        # If hunter eats, add 1 to the width and height and resets the counter.  Also makes eaten counter equal to eaten objects.
        elif len(self.obj_eaten) != self.eaten_counter:
            self._width += 1
            self._height += 1
            self.temp_counter = 0
            self.eaten_counter = len(self.obj_eaten)
        
        self._close_items = []
        self._all_distances = set()
        self._smallest = 0
        
        self.move()
        
        return self.obj_eaten