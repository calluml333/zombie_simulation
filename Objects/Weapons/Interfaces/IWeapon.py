import abc


class IWeapon(abc.ABC):
    @property
    @abc.abstractmethod
    def damage(self):
        pass

    @property
    @abc.abstractmethod
    def speed_decrease(self):
        pass

    @property
    @abc.abstractmethod
    def selected(self):
        pass  