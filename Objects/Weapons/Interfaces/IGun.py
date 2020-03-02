from IWeapon import IWeapon


class IGun(IWeapon):
    @property
    @abc.abstractmethod
    def range(self):
        pass

    @property
    @abc.abstractmethod
    def accuracy(self):
        pass