#!/usr/bin/python
class Component:
    ('This is the component class that will be used to descibe\
    each component (shape) in a certain frame')
    size=1.0
    orientation=0
    reflection=0
    name=''
    def __init__(self,name_val,size_val,orientation_val,reflection_val):
        self.name=name_val
        self.size=size_val
        self.orientation=orientation_val
        self.reflection=reflection_val

    def __str__(self):
        print 'Name=',self.name+' Size is ',self.size.__str__()+' Orientation is ',self.orientation.__str__()+' Reflection is ',self.reflection.__str__()
        

######### END OF Component definition#######

class Frame:
    ' The frame class descibes everything in the frame'
    
    # The list of components
    list_of_comp=[]

    # Relative position of different components in this frame. This is
    # arranged as a dictionary of list of tuples.
    
    relative_positions={'LEFT':[],'ABOVE':[],'INSIDE':[],'OUTSIDE':[]}
    
    def __init__(self):
        self.list_of_comp=[]
        self.relative_positions={'LEFT':[],'ABOVE':[],'INSIDE':[],'OUTSIDE':[]}
        

############ END OF  Frame definition########
    
    
    
