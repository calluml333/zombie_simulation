import abc

class IElement(abc.ABC):
    @property
    @abc.abstractmethod
    def color(self):
        pass

    @property
    @abc.abstractmethod
    def size(self):
        pass

    @property
    @abc.abstractmethod
    def x(self):
        pass

    @property
    @abc.abstractmethod
    def y(self):
        pass
