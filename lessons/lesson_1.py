class Car:
    # конструктор/инициализатор
    def __init__(self, color, model="Mark 2"):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"in drive_to {destination}")
        print(f"Машина модели: {self.model} едет в {destination}")

# github.com

# инициализация объектов
car1 = Car("белый")
car2 = Car("черный", "BMW")
print(car1)
print(car2)
print(type(312312))
print(type(car1))
print(car1.color, car1.model)
print(car2.color, car2.model)
car1.drive_to("Каракол")
car1.color = "серый"
print(car1.color, car1.model)
car2.steering_wheel = "left"
print(car2.steering_wheel, car2.model)
