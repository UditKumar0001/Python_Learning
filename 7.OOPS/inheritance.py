class FactoryMumbai: # Parent Class / super class
    a = "I am an attribute mentioned inside Factory"
    def hello(self):
        print("Hello I am a method mentioned inside Factory")

class FactoryPune(FactoryMumbai): # Child Class / sub class
    pass

obj = FactoryMumbai()

obj2 = FactoryPune()

print(obj.hello())
print(obj2.a)