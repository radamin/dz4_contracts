from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Интерфейс Vehicle(Транспортное средство) обладает минимальным набором методами,
    которые необходимо реализовать в наследующих классах"""
    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def min_fuel_level_sensor(self):
        raise NotImplementedError

    @abstractmethod
    def sensor_reading(self, km: float):
        raise NotImplementedError

    @abstractmethod
    def check_petrol(self, current_liters: float):
        raise NotImplementedError
