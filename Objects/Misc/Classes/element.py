import random
from ..Interfaces.IElement import IElement


class Element(IElement):
    """
    This class defines the basic attributes of the objects in the game
    """

    color = (255,255,255)
    size = 1
    x = None
    y = None
    is_type = 'Element'
    
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.generate_coords()

    def generate_coords(self):
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

    def __add__(self, other):
        rand_threshold = random.random()
        if other.is_type == self.is_type:
            # Same type, do nothing (for now)
            pass    
        
        elif self.is_type == 'Human' and other.is_type == 'Zombie':
            if rand_threshold <= self.p_kill:
                return '0'
            else:
                return '1'
        
        elif self. is_type == 'Human' and other.is_type == 'Weapon':
            if not other.picked_up:
                return '2'

    def check_bounds(self):
        if self.x < 0: 
            self.x = 0
        elif self.x > self.x_boundary: 
            self.x = self.x_boundary
        
        if self.y < 0: 
            self.y = 0
        elif self.y > self.y_boundary: 
            self.y = self.y_boundary
