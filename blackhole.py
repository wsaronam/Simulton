# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    color = 'black'
    radius = 10
    obj_eaten = set()
    
    def __init__(self, x, y, width, height, color):
        
        Simulton.__init__(self, x, y, width, height)
        
        self._x = x
        self._y = y
        self._width = width * 2
        self._height = height * 2
        self._color = color
    
    
    def display(self, canvas):
        canvas.create_oval(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius,
                                fill=self._color)
    
    
    def update(self, model):
        return self.obj_eaten
    
    
    def contains(self, xy):
        if self._x - self._width/2  <= xy[0] <= self._x + self._width/2 and self._y - self._height/2 <= xy[1] <= self._y + self._height/2:
            return xy

               
               
               
