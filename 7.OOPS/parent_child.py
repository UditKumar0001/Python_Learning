class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    pass

animal = Animal("Cheetah")
person = Human("Udit")

person.show()
animal.show()