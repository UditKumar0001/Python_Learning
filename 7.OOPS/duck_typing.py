class Animal:
    def show(self):
        print("Hello I am showing")
class Human():
    def show(self):
        print("Hello i am also showing")

obj = Animal()
obj1 = Human()

obj.show()
obj1.show()