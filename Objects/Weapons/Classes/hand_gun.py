from .weapon import Weapon
import random
import pygame


class HandGun(Weapon):

    # color = (182,182,182)
    weapon_name = 'Hand Gun'
    damage = 0.3
    speed_decrease = 1
    owner = None

    fire_range = 50
    accuracy = 0.8
    shells = random.randint(1, 12)
    target = False
    target_angle = 90 
    selected = False
    
    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self):
        self.y = self.owner.y + (self.owner.size + self.size)
        self.x = self.owner.x
        
    def aim(self, factor):
        self.target_angle = (self.target_angle + (5 * factor)) % 360
        self.target = self.target.rotate(self.target_angle)
        return self.target
