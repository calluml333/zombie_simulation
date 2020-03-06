from ..Interfaces.IGun import IGun
from .weapon import Weapon
import pygame
import math


class Gun(IGun, Weapon):

    # color = (182,182,182)
    weapon_name = 'Gun'
    damage = 0
    speed_decrease = 0

    fire_range = 50
    accuracy = None
    shells = None
    owner_vector = None
    target = False
    target_angle = 0
    selected = False


    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self):
        self.y = self.owner.y + (self.owner.size + self.size)
        self.x = self.owner.x
        self.owner_vector = pygame.math.Vector2(self.owner.x, self.owner.y)
        self.generate_target()
        self. accuracy = 2 * self.fire_range
        
    def aim(self, factor):
        self.current_target = self.owner_vector + self.target.rotate(self.target_angle)
        self.target_angle = (self.target_angle + (factor * 5)) % 360
        return self.current_target

    def generate_target(self):
        self.target = pygame.math.Vector2(round(self.owner.x + self.fire_range*math.cos(math.radians(self.target_angle))), 
                                          round(self.owner.y + self.fire_range*math.sin(math.radians(self.target_angle))))

    def is_agent_in_range(self, agent):
        """
        To check whether an agent (at point C) is in range of the gun, whos owner is at point A
        and target point is at B, we need to carry out three steps:
            1. Check that A, B and C are collinear;
            2. Check that the dot product of (B - A) and (C - A) > 0;
        """
        collinear = self.are_points_collinear(self.owner, self.target, agent, self.accuracy)
        dot_product = self.dot_product_three_points(self.owner, self.target, agent)
        
        if collinear and dot_product > 0:
           return True
        else:
            return False