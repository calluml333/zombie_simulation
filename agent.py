"""
Module that contains the Agent class and relevant subclasses for the zombie outbreak simulation.
"""

class Agent:
    def __init__(self, name, position, speed=0.5):
        self.__name = name
        self.position = position
        self.speed = speed
    
    __agentType = 'a'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if 0 <= value < 100000:
            self.__name = value
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

    
    def __generate_name(self, value):
        print(value)
        if value < 10:
            return self.__agentType + "_0000" + str(value)
        elif 10 <= value < 100:
            return self.__agentType + "_000" + str(value)
        elif 100 <= value < 1000:
            return self.__agentType + "_00" + str(value)
        elif 1000 <= value < 10000:
            return self.__agentType + "_0" + str(value)
        elif 10000 <= value < 100000:
            return self.__agentType + "_" + str(value)
        elif value < 0 or value > 100000:
            raise ValueError("The id value must be of type int and in the range [0, 100000]")
        elif type(value) != int:
            raise TypeError("The id value must be of type int and in the range [0, 100000)")
        
    def move_position(self, neighbour_position):
        self._position = tuple([sum(x) for x in zip(self._position, neighbour_position)])
        
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
    def __init__(self, obj_id, position, speed=0.7):
        Agent.__init__(self, obj_id, position, speed)
        self.agent_type = 'h'


class Zombie(Agent):
    def __init__(self, obj_id, position, speed=0.3):
        Agent.__init__(self, obj_id, position, speed)
        self.agent_type = 'z'


# new = Agent(1,(2,3))
# print(new.name)
# print(new.position)
# print(new.speed)
# new.name = 2
# print(new.name)