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

    @staticmethod
    def are_points_collinear(a, b, c, tolerance=0):
        """
        to check if points a, b, and c are collinear, we just need to make sure that 
        the area of the triangle created by a, b and c is equal to 0, or below some 
        tolerance.
        """
        
        area = abs((a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2)
        print("Area of a: {0} || b: {1} || c: {2} || is {3} || Tolerance: {4} || Colinear?: {5}".format((a.x, a.y), (b.x, b.y), (c.x, c.y), area, tolerance, area < tolerance))
        return  area < tolerance

    def dot_product_three_points(self, a, b, c):
        v1 = (c.x - a.x, c.y - a.y)
        v2 = (b.x - a.x, b.y - a.y)
        dp = self.dot_product(v1, v2)
        print("V1:", v1, "|| V2:", v2, "|| DP:", dp)
        return dp

    @staticmethod
    def dot_product(v1, v2):
        return (v1[0] * v2[0]) + (v1[1] * v2[1])
