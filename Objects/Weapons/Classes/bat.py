from .weapon import Weapon


class Bat(Weapon):

    color = (180,150,70)
    is_type = 'Weapon'
    weapon_type = 'Bat'
    size = 3
    damage = 0.1
    speed_decrease = 0
    owner_id = None
    
    def __init__(self, x_bounday, y_boundary):
        Weapon.__init__(self, x_bounday, y_boundary)


