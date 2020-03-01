from .agent import Agent


class Human(Agent):
    """
    A subclass  of agent, specifying a "Human" agent and it's behaviour.
    """

    color = (150,150,255) 
    is_type = 'Human'
    _player = False
    _has_weapon = False
    _weapons = {}

    def __init__(self, x_boundary, y_boundary, p_kill, speed=7):
        Agent.__init__(self, x_boundary, y_boundary, speed)
        self.p_kill = p_kill
        
    @property
    def is_player(self):
        return self._player

    @is_player.setter
    def is_player(self, value):
        self._player = value

    @property
    def weapons(self):
        return self._weapons

    def update_p_kill(self, value):
        new_p_kill = self.p_kill + value
        if new_p_kill < 1:
            self.p_kill = new_p_kill
            
    def pick_up_weapon(self, weapon):
        self.update_p_kill(weapon.damage)
        self.change_speed(weapon.speed_decrease)
        self._has_weapon = True

    def drop_weapon(self, weapon):	
        self.update_p_kill(-weapon.damage)
        self.change_speed(-weapon.speed_decrease)
        del weapons[weapon.__class__.__name__]
        self._has_weapon = False

    def move_position(self, neighbour_position):
        self.x += neighbour_position[0]
        self.y += neighbour_position[1]
        if self._has_weapon:
            for weapon_id in _weapons:
                _weapons[weapon_id].track_agent(self.position)
                

    