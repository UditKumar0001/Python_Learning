def decorator(func):
    def wrapper():
        print("I will print myself before the function hello ")
        func()
        print("I will print after the function")

    return wrapper

@decorator
def hello():
    print("Hello I am Udit Kumar")

hello()