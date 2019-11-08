"""
Module that contains the various required classes.
"""

class Environment:
    """
    A class that defines the behaviour of the environment that will be used 
    for the simulation.
    """
    def __init__(self, x, y, n_humans, n_zombies):
        self.x = x
        self.y = y
        self.n_humans = n_humans
        self.n_zombies = n_zombies

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if type(value) == int or type(value) == float:
            self._x = value
        else:
            raise TypeError("x is required to be either an int or a float")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if type(value) == int or type(value) == float:
            self._y = value
        else:
            raise TypeError("y is required to be either an int or a float")


class Agent:
    """
    A class that defines the behaviour of the agents that are interacting within the
    environment during the simulation.
    """
    def __init__(self, name, position, speed=0.5):
        self._name = name
        self.position = position
        self.speed = speed
    
    __agentType = 'a'
    colour = (0, 0, 0)

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
        

class Human(Agent):
    """
    A subclass  of agent, specifying a "Human" agent and it's behaviour.
    """
    def __init__(self, name, position, speed=0.7):
        Agent.__init__(self, name, position, speed)
        self.__agent_type = 'h'


class Zombie(Agent):
    """
    A subclass  of agent, specifying a "Zpmbie" agent and it's behaviour.
    """
    def __init__(self, name, position, speed=0.3, was_human=False):
        Agent.__init__(self, name, position, speed )
        self.__agent_type = 'z'
        self.was_human = was_human


if __name__ == "__main__":
    pass