from .IWeapon import IWeapon
import abc


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

    @property
    @abc.abstractmethod
    def target(self):
        pass

    @property
    @abc.abstractmethod
    def target_angle(self):
        pass

    @abc.abstractmethod
    def aim(self, factor):
        pass

    @abc.abstractmethod
    def generate_target(self):
        pass