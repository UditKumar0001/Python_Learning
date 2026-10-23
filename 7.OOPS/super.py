class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name) # super function targets the parents class
        self.age = age
    def show(self):
        print(f"hello your name is {self.name} and your age is {self.age}")

animal = Animal("Cheetah")
person = Human("Udit", 21)

person.show()
animal.show()