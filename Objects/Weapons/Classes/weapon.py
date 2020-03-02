from ..Interfaces.IWeapon import IWeapon
from ...Misc.Classes.element import Element


class Weapon(IWeapon, Element):
    """
    A base class for all weapon types.
    """

    color = (0,255,0)
    is_type = 'Weapon'
    size = 0
    picked_up = False
    damage = 0
    speed_decrease = 0

    def __init__(self, x_boundary, y_boundary):
        Element.__init__(self, x_boundary, y_boundary)
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
   
    def track_agent(self, agent):

        self.y = agent.position[1]
        self.x = agent.position[0]

