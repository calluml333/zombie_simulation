import abc


class IWeapon(abc.ABC):
    @property
    @abc.abstractmethod
    def _damage(self):
        pass

    @property
    @abc.abstractmethod
    def _speed_decrease(self):
        pass

    