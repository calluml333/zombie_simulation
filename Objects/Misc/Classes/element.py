import random
from ..Interfaces.IElement import IElement


class Element(IElement):
    color = (255,255,255)
    size = 1
    x = None
    y = None
    
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.generate_coords()

    def generate_coords(self):
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

    def __add__(self, other):
        rand_threshold = random.random()
        if type(other) == type(self):
            # Same type, do nothing (for now)
            pass    
        elif self.__class__.__name__ == 'Human' and other.__class__.__name__ == 'Zombie':
            if rand_threshold <= self.p_kill:
                print('Zombie has been killed by Human')
                return '0'
            else:
                print('Human has been bitten and is now a Zombie')
                return '1'
