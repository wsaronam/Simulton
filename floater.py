# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from prey import Prey
import random


class Floater(Prey):
    radius = 5
    speed = 5
    color = 'red'
    
    def __init__(self, x, y, width, height, speed, angle, color):
        
        Prey.__init__(self, x, y, width, height, angle, speed)
        
        self._x = x
        self._y = y
        self._width = width * 2
        self._height = height * 2
        self._speed = speed
        self._angle = angle
        self._color = color
        
        Prey.randomize_angle(self)
    
    
    def update(self, model):
        
        if random.uniform(0, 1) <= .3:
            self._angle += round(random.uniform(-.5, .5), 1)
            self._speed += round(random.uniform(-.5, .5), 1)
            
        if self._speed < 3:
            self._speed = 3
        elif self._speed > 7:
            self._speed = 7
        
        Prey.move(self)
    
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)