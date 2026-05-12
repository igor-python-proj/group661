class Animal:
    def move(self):
        print("животное двигается")


# PEP8
class Swimming(Animal):
    def move(self):
        super().move()
        print("плавает")


class Flying(Animal):
    def move(self):
        super().move()
        print("летает")


class Duck(Flying, Swimming):
    def move(self):
        super().move()
        print("утка плавает и летает")


duck = Duck()
duck.move()
print(Duck.__mro__) # method resolution order

bird = Flying()
bird.move()
print(Flying.__mro__) # method resolution order
