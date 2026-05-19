class Car:
    # конструктор/инициализатор
    def __init__(self, color, model="Mark 2"):
        self.color = color
        self.model = model
        self._fined = False
        self.__max_speed = 0

    def _calculated_fuel(self):
        print(self.color)
        return 1

    def __test(self):
        print(self.color)

    def drive_to(self, destination):
        # print(f"in drive_to {destination}")
        if not self._calculated_fuel():
            print("нет топлива")
        print(f"Машина модели: {self.model} едет в {destination}, "
              f"Оштрафован:", "да" if car1._fined else "нет")

    def change_color(self, new_color):
        self.color = new_color
        print("апвапвапав")

    # геттер - для получения значения приватных атрибутов
    def get_max_speed(self):
        return self.__max_speed

    # сеттер - для установки значения
    def set_max_speed(self, new_speed):
        if new_speed < 0:
            raise ValueError("Новая скорость меньше нуля")
        self.__max_speed = new_speed

    @property
    def max_speed(self):
        # геттер
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new_speed):
        if new_speed < 0:
            raise ValueError("Новая скорость меньше нуля")
        self.__max_speed = new_speed

if __name__ == "__main__":
    car1 = Car("черный", "BMW")
    car2 = Car("белый")
    print(car1.color, car1.model)
    # print(car1.__max_speed) # Ошибка
    car1.drive_to("Кант")
    print("Оштрафован:", "да" if car1._fined else "нет" )
    car1._calculated_fuel()
    car1.__max_speed = 200 # Не настоящий __max_speed из класса
    # print(car2.__max_speed)
    print("Car 1 max_speed: ", car1.get_max_speed())
    car1.set_max_speed(180)
    print("Car 1 max_speed: ", car1.get_max_speed())
    print(f"Car 1 max_speed: {car1.max_speed}")
    car1.max_speed = 200
    print(f"Car 1 max_speed: {car1.max_speed}")

    # name mangling
    print(f"car 1 max_speed private: {car1._Car__max_speed}") # Такое только для тестирования
