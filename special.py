# Special Class;  renamed to "The Punisher" (inspired by the Punisher from Marvel's universe)
# The Punisher moves randomly similar to the Ball object, but it has the ability to
# destroy Black_Holes, Pulsators, and Hunters.  It, however, leaves the Balls and Floaters alone.

from mobilesimulton import Mobile_Simulton



class Special(Mobile_Simulton):
    radius = 20
    speed = 10
    color = 'red'
    
    def __init__(self, x, y, width, height, speed, angle, color):
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)
        
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._speed = speed
        self._angle = angle
        self._color = color
        
        self.randomize_angle()
    
    
    def update(self, model):
        self.move()
    
    
    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius      , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill=self._color)
    
    
    def contains(self, xy):
        if self._x - self._width/2  <= xy[0] <= self._x + self._width/2 and self._y - self._height/2 <= xy[1] <= self._y + self._height/2:
            return xy