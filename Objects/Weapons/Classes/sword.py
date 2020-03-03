from .weapon import Weapon


class Sword(Weapon):

    color = (225,225,225)
    weapon_name = 'Sword'
    size = 3
    damage = 0.2
    speed_decrease = 1
    owner = None
    
    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self, agent):
        self.y = self.owner.y
        self.x = self.owner.x + (agent.size + self.size)