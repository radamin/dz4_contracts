from Car import Car
from Driving import Driving


def main():
    # Пример использования программы
    car = Car("Truck", 1000, 700, 35)   # Создан грузовик
    driving = Driving(car)   # Создан модуль управления
    driving.start_vehicle()   # Запуск двигателя
    driving.driving(1950)   # Отправлен в рейс
    driving.stop_vehicle()   # выключение зажигания
    driving.driving(50)   # Попытка поехать с выключенным зажиганием


if __name__ == '__main__':
    main()
