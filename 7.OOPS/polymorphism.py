# Method Overloading doesn't exist in python

# Method Overriding
class Animal:
    def show(self):
        print("Hello I am Panda")

class Human(Animal):
    def show(self):
        print("how are you?")

obj = Human()
obj.show()