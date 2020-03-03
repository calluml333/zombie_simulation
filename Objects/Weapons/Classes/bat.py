from .weapon import Weapon


class Bat(Weapon):

    color = (180,150,70)
    weapon_name = 'Bat'
    damage = 0.1
    speed_decrease = 1
    owner = None
    
    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self, agent):
        self.y = self.owner.y
        self.x = self.owner.x - (agent.size + self.size)


