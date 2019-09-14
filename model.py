import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
import math

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
obj_kind = None
running     = False
cycle_count = 0
balls       = set()



#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just 1 update in the simulation
def step ():
    
    global cycle_count
    cycle_count += 1
        
    for b in balls.copy():

        if type(b) == Black_Hole:
            temp_set = set()
            for obj in balls:
                if type(obj) == Ball or type(obj) == Floater:
                    temp_set.add(obj)
            for obj in temp_set:
                ans = b.contains(obj.get_location())
                if ans != None:
                    b.obj_eaten.add(obj)
                    balls.remove(obj)
            b.update(model)        
            
        elif type(b) == Pulsator:
            temp_set = set()
            for obj in balls:
                if type(obj) == Ball or type(obj) == Floater:
                    temp_set.add(obj)
            for obj in temp_set:
                ans = b.contains(obj.get_location())
                if ans != None:
                    b.obj_eaten.add(obj)
                    balls.remove(obj)
            updated = b.update(model)    
            if updated == 'Dead':
                balls.remove(b)
            else:
                updated
        
        elif type(b) == Hunter:
            temp_set = set()
            for obj in balls:
                if type(obj) == Ball or type(obj) == Floater:
                    temp_set.add(obj)
            for obj in temp_set:
                ans = b.contains(obj.get_location())
                if ans != None:
                    b.obj_eaten.add(obj)
                    balls.remove(obj)
                close = Hunter.distance(b, obj.get_location())
                if close <= b.vision:
                    b._close_items.append((obj, close))
            
            try:
                b._smallest = b._close_items[0]
                for obj, dist in b._close_items:
                    if dist < b._smallest[1]:
                        b._smallest = (obj,dist)
                b.set_angle(math.atan2(b._smallest[0].get_location()[1] - b.get_location()[1], b._smallest[0].get_location()[0] - b.get_location()[0]))
            except:
                pass
            
            updated = b.update(model)
            if updated == 'Dead':
                balls.remove(b)
            else:
                updated
        
        elif type(b) == Special:
            temp_set = set()
            for obj in balls:
                if type(obj) == Black_Hole or type(obj) == Pulsator or type(obj) == Hunter:
                    temp_set.add(obj)
            for obj in temp_set:
                ans = b.contains(obj.get_location())
                if ans != None:
                    balls.remove(obj)
            updated = b.update(model)    
            if updated == 'Dead':
                balls.remove(b)
            else:
                updated
        
        else:         
            b.update(model)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global obj_kind
    obj_kind = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    
    if obj_kind == 'Remove':
        for obj in balls.copy():
            left = obj.get_location()[0] - (obj.get_dimension()[0] / 2)
            right = obj.get_location()[0] + (obj.get_dimension()[0] / 2)
            up = obj.get_location()[1] + (obj.get_dimension()[1] / 2)
            down = obj.get_location()[1] - (obj.get_dimension()[1] / 2)
            
            if left <= x <= right:
                if down <= y <= up:
                    balls.remove(obj)

            
    else:
        working_obj = eval(obj_kind)
        if obj_kind == 'Ball' or obj_kind == 'Floater' or obj_kind == 'Special':
            balls.add(working_obj(x, y, working_obj.radius, working_obj.radius, working_obj.speed, 0, working_obj.color))
        
        elif obj_kind == 'Black_Hole':
            balls.add(working_obj(x, y, working_obj.radius, working_obj.radius, working_obj.color))
        
        elif obj_kind == 'Pulsator':
            balls.add(Pulsator(x, y, working_obj.radius, working_obj.radius, working_obj.color))
        
        elif obj_kind == 'Hunter':
            balls.add(working_obj(x, y, working_obj.radius, working_obj.radius, working_obj.speed, 0, working_obj.color))

            
            




#add simulton s to the simulation
def add(s):
    pass
    

# remove simulton s from the simulation    
def remove(s):
    pass
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    temp = set()
    
    for obj in balls:
        if p(obj):
            temp.add(obj)
    
    return temp


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        
        for b in balls.copy():
    
            if type(b) == Black_Hole:
                temp_set = set()
                for obj in balls:
                    if type(obj) == Ball or type(obj) == Floater:
                        temp_set.add(obj)
                for obj in temp_set:
                    ans = b.contains(obj.get_location())
                    if ans != None:
                        b.obj_eaten.add(obj)
                        balls.remove(obj)
                b.update(model)        
                
            elif type(b) == Pulsator:
                temp_set = set()
                for obj in balls:
                    if type(obj) == Ball or type(obj) == Floater:
                        temp_set.add(obj)
                for obj in temp_set:
                    ans = b.contains(obj.get_location())
                    if ans != None:
                        b.obj_eaten.add(obj)
                        balls.remove(obj)
                updated = b.update(model)    
                if updated == 'Dead':
                    balls.remove(b)
                else:
                    updated
            
            elif type(b) == Hunter:
                temp_set = set()
                for obj in balls:
                    if type(obj) == Ball or type(obj) == Floater:
                        temp_set.add(obj)
                for obj in temp_set:
                    ans = b.contains(obj.get_location())
                    if ans != None:
                        b.obj_eaten.add(obj)
                        balls.remove(obj)
                    close = Hunter.distance(b, obj.get_location())
                    if close <= b.vision:
                        b._close_items.append((obj, close))
                
                try:
                    b._smallest = b._close_items[0]
                    for obj, dist in b._close_items:
                        if dist < b._smallest[1]:
                            b._smallest = (obj,dist)
                    b.set_angle(math.atan2(b._smallest[0].get_location()[1] - b.get_location()[1], b._smallest[0].get_location()[0] - b.get_location()[0]))
                except:
                    pass
                
                updated = b.update(model)
                if updated == 'Dead':
                    balls.remove(b)
                else:
                    updated
            
            elif type(b) == Special:
                temp_set = set()
                for obj in balls:
                    if type(obj) == Black_Hole or type(obj) == Pulsator or type(obj) == Hunter:
                        temp_set.add(obj)
                for obj in temp_set:
                    ans = b.contains(obj.get_location())
                    if ans != None:
                        balls.remove(obj)
                updated = b.update(model)    
                if updated == 'Dead':
                    balls.remove(b)
                else:
                    updated
            
            else:         
                b.update(model)
                


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
