from .weapon import Weapon


class Bat(Weapon):

    color = (180,150,70)
    _damage = 1
    _speed_decrease = 0
    
    def __init__(self, x_bounday, y_boundary):
        Element.__init__(self, x_bounday, y_boundary)
        Weapon.__init__(self, x_bounday, y_boundary)


