from .gun import Gun
import random
import pygame
import math


class HandGun(Gun):

    # color = (182,182,182)
    weapon_name = 'Hand Gun'
    damage = 0.3
    speed_decrease = 1

    accuracy = None
    fire_range = 100
    shells = random.randint(1, 12)

    def __init__(self, x_bounday, y_boundary):
        Gun.__init__(self, x_bounday, y_boundary)
