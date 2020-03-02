from .weapon import Weapon


class Bat(Weapon):

    color = (180,150,70)
    is_type = 'Weapon'
    weapon_name = 'Bat'
    size = 3
    damage = 0.1
    speed_decrease = 1
    owner = None
    
    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)

    def track_agent(self, agent):
        self.y = agent.position[1]
        self.x = agent.position[0] - (agent.size + self.size)


