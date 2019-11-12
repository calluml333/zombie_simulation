"""
Module that contains the various required classes for agents in the simulation.
"""

import random 

class Agent:
    """
    A class that defines the behaviour of the agents that are interacting within the
    environment during the simulation.
    """

    agent_type = 'a'
    color = (0, 0, 0)
    size = 5
    
    def __init__(self, x_boundary, y_boundary, speed=5):
        self._speed = speed
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
             
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if 0.0 < value <= 1.0:
            self._speed = value
        elif value <= 0.0:
            raise ValueError("Speed must be (0,)")
        elif type(value) != int:
            raise TypeError("Speed must be either an integer or a float")   
    
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
        
        

class Human(Agent):
    """
    A subclass  of agent, specifying a "Human" agent and it's behaviour.
    """

    color = (0,0,255) 

    def __init__(self, x_boundary, y_boundary, speed=7):
        Agent.__init__(self, x_boundary, y_boundary, speed)
        self.agent_type = 'h'

    def __add__(self, other_blob):
        if other_blob.agent_type == self.agent_type:
            # Same type, do nothing
            pass    
        elif other_blob.agent_type == 'z':
            # Human-Zombie interaction  
            pass
        else:
            # Some other interaction
            pass


class Zombie(Agent):
    """
    A subclass  of agent, specifying a "Zombie" agent and it's behaviour.
    """
    
    color = (255,0,0)

    def __init__(self, x_boundary, y_boundary, speed=3, was_human=False):
        Agent.__init__(self, x_boundary, y_boundary, speed)
        self.agent_type = 'z'
        self.was_human = was_human


if __name__ == "__main__":
    pass