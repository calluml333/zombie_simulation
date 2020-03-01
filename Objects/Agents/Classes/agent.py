import random 
import math
import numpy as np
from ...Misc import Element
from ..Interfaces.IAgent import IAgent


class Agent(Element, IAgent):
    """
    A class that defines the behaviour of the agents that are interacting within the
    environment during the simulation.
    """

    color = (0, 0, 0)
    is_type = 'Agent'
    size = 7
    _sight = 200
    
    def __init__(self, x_boundary, y_boundary, speed):
        Element.__init__(self, x_boundary, y_boundary)
        self._speed = speed
        
    @property
    def speed(self):
        return self._speed

    def change_speed(self, value):
        if 0 < self.speed + value < 10:
            self._speed += value
        elif value <= 0 or value > 10:
            raise ValueError("Speed must be an int from the range (0, 10]")
        elif type(value) != int:
            raise TypeError("Speed must be an int from the range (0, 10]")

    @property
    def position(self):
        return (self.x, self.y)

    @position.setter
    def position(self, new_position):
        self.x, self.y = new_position

    @property
    def sight(self):
        return self._sight

    @sight.setter
    def sight(self, value):
        self._sight = value
    
    def move_position(self, neighbour_position):
        self.x += neighbour_position[0]
        self.y += neighbour_position[1]

    def move_north(self):
        self.y += self._speed * -1

    def move_east(self):
        self.x += self._speed * 1

    def move_south(self):
        self.y += self._speed * 1

    def move_west(self):
        self.x += self._speed * -1

    def calc_distance_to_agent(self, agent):
        self_coords = (self.x, self.y)
        agent_cords = (agent.x, agent.y)
        return np.sqrt(sum([(a - b) ** 2 for a, b in zip(self_coords, agent_cords)]))
              
    def find_nearest_human(self, population):
        nearest_human = False
        smallest_distance = 1e30

        for member_id in population:
            member = population[member_id]
            if member.is_type == 'Human':
                distance = self.calc_distance_to_agent(member)
                if distance < smallest_distance:
                    nearest_human = member
                    smallest_distance = distance
        
        return nearest_human, smallest_distance

    def move_towards_agent(self, other_agent):
        x = (other_agent.x - self.x)
        y = (other_agent.y - self.y)
        theta = np.arctan2(other_agent.y - self.y, other_agent.x - self.x)

        dx = round(self._speed * math.cos(theta))
        dy = round(self._speed * math.sin(theta))
        self.move_position((dx, dy))


if __name__ == "__main__":
    pass
