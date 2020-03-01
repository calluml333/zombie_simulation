from .agent import Agent


class Human(Agent):
    """
    A subclass  of agent, specifying a "Human" agent and it's behaviour.
    """

    color = (150,150,255) 
    is_type = 'Human'
    p_kill = 0.5
    is_player = False
    speed = 7
    _has_weapon = False
    _weapons = {}

    def __init__(self, x_boundary, y_boundary):
        Agent.__init__(self, x_boundary, y_boundary)

    @property
    def weapons(self):
        return self._weapons

    def update_p_kill(self, value):
        new_p_kill = self.p_kill + value
        if new_p_kill < 1:
            self.p_kill = new_p_kill
            
    def pick_up_weapon(self, weapon):
        if weapon.weapon_name not in list(self.weapons):
            self.update_p_kill(weapon.damage)
            self.increment_speed(-weapon.speed_decrease)
            self._has_weapon = True
            self.weapons[weapon.weapon_name] = weapon
            weapon.picked_up = True
            weapon.owner = self
            print('Human has picked up a', weapon.weapon_name)

    def drop_weapon(self, weapon):
        if weapon.weapon_name in list(self.weapons):	
            self.update_p_kill(-weapon.damage)
            self.increment_speed(weapon.speed_decrease)
            weapon.picked_up = False
            weapon.owner = None
            del self.weapons[weapon.weapon_name]
        if not self.weapons:
            self._has_weapon = False

    def drop_all_weapons(self):
        weapon_ids = list(self.weapons.keys())
        for weapon_id in weapon_ids:
            self.drop_weapon(self.weapons[weapon_id])

    def move_position(self, neighbour_position):
        self.x += neighbour_position[0]
        self.y += neighbour_position[1]
        if self._has_weapon:
            for weapon_id in _weapons:
                _weapons[weapon_id].track_agent(self.position)
                

    