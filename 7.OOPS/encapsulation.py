# encapsulation means putting data(variables) and code(functions) together in one place - inside a class.

class Factory:
    __a = "Pune" # __ => symbolise private

    def __show(self):
        print("Hello I am in Pune Factory")

class Bhopal(Factory):
    def show2(self):
        print(super().__a)

obj = Bhopal()
obj.show2()
    