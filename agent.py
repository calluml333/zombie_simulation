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
    
    def __init__(self, x_boundary, y_boundary, speed=0.5):
        # self._name = name
        # self.position = position
        self.speed = speed
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.position = (random.randrange(0, self.x_boundary), random.randrange(0, self.y_boundary))
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if 0 <= value < 100000:
            self._name = value
        elif value < 0 or value > 100000:
            raise ValueError("The id value must be of type int and in the range [0, 100000]")
        elif type(value) != int:
            raise TypeError("The id value must be of type int and in the range [0, 100000)")
 
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (type(value) is list or type(value) is tuple) and len(value) == 2:
            self._position = value
        elif (type(value) is not list and type(value) is not tuple):
            raise TypeError("The position must be given as a list or tuple")
        elif len(value) != 2:
            raise ValueError("The position must be 2-dimensional")
          
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if 0.0 < value <= 1.0:
            self._speed = value
        elif value <= 0.0 or speed > 1.0 :
            raise ValueError("Speed must be in the range (0, 1]")
        elif type(value) != int:
            raise TypeError("Speed must be either an integer or a float")   
    
    def move_position(self, neighbour_position):
        self._position = tuple([sum(x) for x in zip(self._position, neighbour_position)])

    def check_bounds(self):
        if self.position[0] < 0: 
            self.position[0] = 0
        elif self.position[0] > self.x_boundary: 
            self.position[0] = self.x_boundary
        
        if self.position[1] < 0: 
            self.position[1] = 0
        elif self.position[1] > self.y_boundary: 
            self.position[1] = self.y_boundary
        

class Human(Agent):
    """
    A subclass  of agent, specifying a "Human" agent and it's behaviour.
    """

    color = (0,0,255) 

    def __init__(self, x_boundary, y_boundary, speed=0.7):
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

    def __init__(self, x_boundary, y_boundary, speed=0.3, was_human=False):
        Agent.__init__(self, x_boundary, y_boundary, speed )
        self.agent_type = 'z'
        self.was_human = was_human


if __name__ == "__main__":
    pass