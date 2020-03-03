from IWeapon import IWeapon


class IGun(IWeapon):
    @property
    @abc.abstractmethod
    def fire_range(self):
        pass

    @property
    @abc.abstractmethod
    def accuracy(self):
        pass

    @property
    @abc.abstractmethod
    def shells(self):
        pass