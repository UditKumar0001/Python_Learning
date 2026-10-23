class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello how are you and your name is: {self.name}"

    def __add__(self, other):
        return f"Your sum of your ages is: {self.age + other.age}"

obj = Animal("Cheetah", 12)
obj2 = Animal("Dolphin", 8)
print(obj + obj2)