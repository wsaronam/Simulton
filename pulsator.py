# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter = 30
    color = 'black'
    radius = 10
    
    
    def __init__(self, x, y, width, height, color):
        
        Black_Hole.__init__(self, x, y, width, height, color)
        
        self._x = x
        self._y = y
        self._width = width * 2
        self._height = height * 2
        self._color = color
        self.temp_counter = 0
        self.eaten_counter = 0
        self.obj_eaten = set()
    
    
    def display(self, canvas):

        canvas.create_oval(self._x-(self._width/2)     , self._y-(self._height/2),
                                self._x+(self._width/2), self._y+(self._height/2),
                                fill=self._color)

    
    
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
        
        # If pulsator doesn't eat, add 1 to the counter.
        if len(self.obj_eaten) == self.eaten_counter:
            self.temp_counter += 1
            
        # If pulsator eats, add 1 to the width and height and resets the counter.  Also makes eaten counter equal to eaten objects.
        elif len(self.obj_eaten) != self.eaten_counter:
            self._width += 1
            self._height += 1
            self.temp_counter = 0
            self.eaten_counter = len(self.obj_eaten)
        
        return self.obj_eaten
    
    
    
    
    