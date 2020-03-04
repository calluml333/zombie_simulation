from .weapon import Weapon


class Sword(Weapon):

    color = (225,225,225)
    weapon_name = 'Sword'
    size = 3
    damage = 0.2
    speed_decrease = 1
    
    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self):
        self.y = self.owner.y
        self.x = self.owner.x + (self.owner.size + self.size)