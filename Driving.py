class Driving:
    """Класс вождения"""

    def __init__(self, vehicle):
        self.vehicle = vehicle

    def start_vehicle(self):
        self.vehicle.start()

    def __drive(self, km: int):
        """Метод вождения транспортным средством.
        Каждые 10 километров будут выводиться данные с датчиков и сообщения о неисправностях"""
        for i in range(1, km + 1):
            self.vehicle.current_fuel_level -= self.vehicle.fuel_consumption * 0.01
            if i % 10 == 0 or i == km:
                self.vehicle.min_fuel_level_sensor()
                self.vehicle.sensor_reading(i)
            c_f_l = self.vehicle.current_fuel_level
            self.vehicle.check_petrol(c_f_l)

    def driving(self, km: int):
        """Метод проверки работы мотора перед движением транспорта"""
        if self.vehicle.engine_ON:
            self.__drive(km)
        else:
            print("Двигатель не запущен")

    def stop_vehicle(self):
        self.vehicle.stop()
