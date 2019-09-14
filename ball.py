# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    speed = 5
    color = 'blue'
    
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
        Prey.move(self)
    
    
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)
        
        