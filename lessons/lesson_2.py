# родительский класс, суперкласс
class Car:
    # конструктор/инициализатор
    def __init__(self, color, model="Mark 2"):
        self.color = color
        self.model = model
        self.max_speed = 0

    def drive_to(self, destination):
        # print(f"in drive_to {destination}")
        print(f"Машина модели: {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print("апвапвапав")

# дочерний класс, наследник, подкласс
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    def drive_to(self, destination):
        print(f"Автобус едет в рейс в {destination}")
        super().drive_to(destination) # это обращение к методу из родит. класса

class Truck(Car):
    def change_color(self, new_color):
        self.color = new_color
        print(f"цвет грузовика изменился на {new_color}")

car2 = Car("черный", "BMW")
car2.change_color("серый")
bus_42 = Bus("зеленый", "Mercedes", "42")
print(bus_42.color, bus_42.model, bus_42.number)
bus_42.drive_to("Сокулук")
truck1 = Truck("красный", "Man")
truck1.change_color("синий")
truck1.drive_to("Каракол")
car2.drive_to("Бишкек")

print(type(truck1))
print(isinstance(truck1, Truck))
print(isinstance(bus_42, Car))

vehicles = [car2, truck1, bus_42]
for v in vehicles:
    v.drive_to(destination="Каракол")


