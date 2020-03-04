from .weapon import Weapon
import random
import pygame
import math


class HandGun(Weapon):

    # color = (182,182,182)
    weapon_name = 'Hand Gun'
    damage = 0.3
    speed_decrease = 1

    fire_range = 50
    accuracy = 0.8
    shells = random.randint(1, 12)
    owner_vector = None
    target = False
    target_angle = 90
    selected = False


    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self):
        self.y = self.owner.y + (self.owner.size + self.size)
        self.x = self.owner.x
        self.owner_vector = pygame.math.Vector2(self.owner.x, self.owner.y)
        self.generate_target()
        
    def aim(self, factor):
        self.current_target = self.owner_vector + self.target.rotate(self.target_angle)
        self.target_angle = (self.target_angle + 5) % 360
        return self.current_target

    def generate_target(self):
        self.target = pygame.math.Vector2(round(self.owner.x + self.fire_range*math.cos(math.radians(self.target_angle))), 
                                          round(self.owner.y + self.fire_range*math.sin(math.radians(self.target_angle))))
