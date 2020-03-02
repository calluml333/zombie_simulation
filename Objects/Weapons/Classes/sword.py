from .weapon import Weapon


class Sword(Weapon):

    color = (225,225,225)
    is_type = 'Weapon'
    weapon_name = 'Sword'
    size = 3
    damage = 0.3
    speed_decrease = 1
    owner = None
    
    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self, agent):
        self.y = agent.position[1]
        self.x = agent.position[0] + (agent.size + self.size)