import random
from ..Interfaces.IElement import IElement


class Element(IElement):
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
                print('Zombie has been killed by Human')
                return '0'
            else:
                print('Human has been bitten and is now a Zombie')
                return '1'
        
        elif self. is_type == 'Human' and other.is_type == 'Weapon':
            if not other.picked_up:
                print('Human has picked up a', other.weapon_type)
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
