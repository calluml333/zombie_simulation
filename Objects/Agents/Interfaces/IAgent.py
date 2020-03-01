import abc
from ...Misc.Interfaces.IElement import IElement

class IAgent(IElement):
    @property
    @abc.abstractmethod
    def _sight():
        pass

    @property
    @abc.abstractmethod
    def speed():
        pass

    @property
    @abc.abstractmethod
    def position(self):
        return (self.x, self.y)

    @property
    @abc.abstractmethod
    def sight(self):
        return self._sight

    @abc.abstractmethod
    def move_position(self, neighbour_position):
        pass

    @abc.abstractmethod
    def check_bounds(self):
        pass

    @abc.abstractmethod
    def move_north(self):
        pass

    @abc.abstractmethod
    def move_east(self):
        pass

    @abc.abstractmethod
    def move_south(self):
        pass

    @abc.abstractmethod
    def move_west(self):
        pass

    @abc.abstractmethod
    def calc_distance_to_agent(self, agent):
        pass
              
    @abc.abstractmethod
    def find_nearest_human(self, human_dict):
        pass

    @abc.abstractmethod
    def move_towards_agent(self, other_agent):
        pass