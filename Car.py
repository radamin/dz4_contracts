from contracts import contract
from colorama import Fore

from Vehicle import Vehicle


def emergency_stop(func):
    """
    Функция используется как контрактная.
    Если параметр принимаемой функции не будет соответствовать условию value > 0,
    работа программы прервется с ошибкой 'Аварийная остановка. В системе нет топлива'
    Args:
        func (function) : функция
    """
    def f(self, value: float):
        """
        .
        :param self:
        :param value: Значение параметра функции funс
        :return: возвращает значение func
        """
        assert value > 0, "Аварийная остановка. В системе нет топлива"
        return func(self, value)
    return f


class Car(Vehicle):
    """
    Класс Car(автомобиль) наследует все обязательные методы Vehicle
    """

    @contract
    def __init__(self, type_car: str, tank: 'int, >5', current_fuel_level: 'float|int, >=0', fuel_consumption: 'float|int, >0.1'):
        """
        Метод инициализации. Имеет декоратор метода contract из библиотеки contracts.
        При невалидном вводе данных при создании класса, программа прекратит работу с ошибкой.
        Значение tank не может быть меньше 5.
        Если значение current_fuel_level будет превышать значение tank,
        значение current_fuel_level будет приравнено значению tank.

        :param type_car: тип автомобиля
        :param tank: объем бака
        :param current_fuel_level: текущий уровень топлива
        :param fuel_consumption: расход топлива на 100 км
        """

        self.type_car = type_car
        self.tank = tank
        if current_fuel_level > tank:
            self.current_fuel_level = tank
        else:
            self.current_fuel_level = current_fuel_level
        self.fuel_consumption = fuel_consumption
        self.engine_ON: bool = False

    def start(self):
        """Метод запуска двигателя"""
        self.engine_ON = True
        print("Двигатель запущен.")

    def stop(self):
        """Метод выключения зажигания"""
        self.engine_ON = False
        print("Двигатель остановлен.")

    def min_fuel_level_sensor(self):
        """Метод контроля уровня топлива и выводящий сообщение о переходе на резервный запас."""
        if self.current_fuel_level < self.tank * 0.15:
            print(f"{Fore.YELLOW}Низкий уровень топлива{Fore.RESET}")

    def sensor_reading(self, km: float):
        """
        Метод выводящий показания одометра и остатка топлива
        :param km: текущее показание одометра
        """
        print(f"{km}км проехал, {self.current_fuel_level:.2f} литров топлива осталось")

    @emergency_stop
    def check_petrol(self, current_liters: float):
        """
        Метод контроля уровня топлива.
        Имеется декоратор с контрактной функцией.
        :param current_liters: Текущий уровень бензобака
        :return:
        """
        pass

print()
