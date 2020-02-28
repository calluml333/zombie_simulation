"""
Module that contains the various required classes for agents in the simulation.
"""

import random 
import math
import numpy as np

class Agent:
    """
    A class that defines the behaviour of the agents that are interacting within the
    environment during the simulation.
    """

    agent_type = 'a'
    color = (0, 0, 0)
    size = 5
    
    def __init__(self, x_boundary, y_boundary, p_kill=0, speed=5):
        self._speed = speed
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.p_kill = p_kill
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

    def __add__(self, other):
        rand_threshold = random.random()
        if other.agent_type == self.agent_type:
            # Same type, do nothing (for now)
            pass    
        elif self.agent_type == 'h' and other.agent_type == 'z':
            if rand_threshold >= self.p_kill:
                other.blank_out_agent()
                return None
            else:
                return self.x, self.y
        elif other.agent == 'r':
            pass

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if 0.0 < value:
            self._speed = value
        elif value <= 0.0:
            raise ValueError("Speed must be (0,)")
        elif type(value) != int:
            raise TypeError("Speed must be either an integer or a float")  

    @property
    def position(self):
        return (self.x, self.y)

    @position.setter
    def position(self, new_position):
        self.x, self.y = new_position
    
    def move_position(self, neighbour_position):
        self.x += neighbour_position[0]
        self.y += neighbour_position[1]

    def check_bounds(self):
        if self.x < 0: 
            self.x = 0
        elif self.x > self.x_boundary: 
            self.x = self.x_boundary
        
        if self.y < 0: 
            self.y = 0
        elif self.y > self.y_boundary: 
            self.y = self.y_boundary

    def blank_out_agent(self):
        self.agent_type == 'r'
        self.color == (255,255,255)
        self.speed == 0
        print('Agent has died')

    def move_north(self):
        self.y += self._speed * -1

    def move_east(self):
        self.x += self._speed * 1

    def move_south(self):
        self.y += self._speed * 1

    def move_west(self):
        self.x += self._speed * -1

    def move_north_east(self):
        self.move_north()
        self.move_east()
        
    def move_south_east(self):
        self.move_south()
        self.move_east()

    def move_north_west(self):
        self.move_north()
        self.move_west()

    def move_south_west(self):
        self.move_south()
        self.move_east()

    def calc_distance_to_agent(self, agent):
        self_coords = (self.x, self.y)
        agent_cords = (agent.x, agent.y)
        return np.sqrt(sum([(a - b) ** 2 for a, b in zip(self_coords, agent_cords)]))
              
    def find_nearest_human(self, human_dict):
        smallest_distance = 1e30
        for human_id in human_dict:
            human = human_dict[human_id]
            distance = self.calc_distance_to_agent(human)
            if distance < smallest_distance:
                nearest_human = human
                smallest_distance = distance
        return nearest_human 

    def move_towards_agent(self, other_agent):
        x = (other_agent.x - self.x)
        y = (other_agent.y - self.y)
        theta = np.arctan2(other_agent.y - self.y, other_agent.x - self.x)
        dx = round(self._speed * math.cos(theta))
        dy = round(self._speed * math.sin(theta))
        self.move_position((dx, dy))


class Human(Agent):
    """
    A subclass  of agent, specifying a "Human" agent and it's behaviour.
    """

    color = (150,150,255) 

    def __init__(self, x_boundary, y_boundary, p_kill=0.7, speed=7):
        Agent.__init__(self, x_boundary, y_boundary, speed)
        self.agent_type = 'h'

    @property
    def p_kill(self):
        return self._p_kill

    @p_kill.setter
    def p_kill(self, value):
        self._p_kill = value


class Zombie(Agent):
    """
    A subclass  of agent, specifying a "Zombie" agent and it's behaviour.
    """
    
    color = (255,0,0)

    def __init__(self, x_boundary, y_boundary, speed=0.00001, was_human=False):
        Agent.__init__(self, x_boundary, y_boundary, speed)
        self.agent_type = 'z'
        self.was_human = was_human

    def hunt_human(self, human_dict):
        nearest_human = self.find_nearest_human(human_dict)
        self.move_towards_agent(nearest_human)


if __name__ == "__main__":
    pass
