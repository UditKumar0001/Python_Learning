class Human:
    def __init__(self, age):
        self.age = age

    def show(self): # instance method
        print("How are you?")

    @classmethod
    def hello(cls): # class method targets the location of the class
        print("How are you?")

    @staticmethod
    def static():
        print("how are you")

obj  = Human(21)
obj.show()
        