name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are a valid voter")

else:
    print(f"Hello {name}, your age is below the voter age limit")