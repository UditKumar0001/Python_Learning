class Animal:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"{self.name}")

class Human:
    def __init__(self, name, age):
        pass

class Robots(Animal, Human):
    name3 = "chalie chaplin"

obj = Robots("Chitti")
obj.show()


