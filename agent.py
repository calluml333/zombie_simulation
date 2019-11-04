"""
Module that contains the Agent class and relevant subclasses for the zombie outbreak simulation.
"""

class Agent:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (type(value) is list or type(value) is tuple) and len(value) == 2:
            self._position = value
        elif (type(value) is not list or type(value) is not tuple):
            raise ValueError("The position must be given as a list or tuple")
        elif len(value) == 2:
            raise ValueError("The position must be 2-dimensional")
          

    def move_north(self):
        self._position = tuple([sum(x) for x in zip(self._position, (-1, 0))])
    
    def move_north_east(self):
        self._position = tuple([sum(x) for x in zip(self._position, (-1, 1))])

    def move_east(self):
        self._position = tuple([sum(x) for x in zip(self._position, (0, 1))])

    def move_south_east(self):
        self._position = tuple([sum(x) for x in zip(self._position, (1, 1))])

    def move_south(self):
        self._position = tuple([sum(x) for x in zip(self._position, (1, 0))])

    def move_south_west(self):
        self._position = tuple([sum(x) for x in zip(self._position, (1, -1))])

    def move_west(self):
        self._position = tuple([sum(x) for x in zip(self._position, (0, -1))])

    def move_north_west(self):
        self._position = tuple([sum(x) for x in zip(self._position, (-1, -1))])


class Human(Agent):
    def __init__(self, name, position):
        Agent.__init__(self, name, position)


class Zombie(Agent):
    def __init__(self, name, position):
        Agent.__init__(self, name, position)