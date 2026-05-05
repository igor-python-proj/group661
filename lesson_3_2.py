from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        pass

# конкретные классы
class Dog(Animal):
    # реализация абс. метода
    def make_sound(self):
        print("Вав вав")

    def test(self):
        print("тест в классе собаки")

class Cat(Animal):
    def test(self):
        print("test in cat")

puppy = Dog()
puppy.make_sound()
kitty = Cat()