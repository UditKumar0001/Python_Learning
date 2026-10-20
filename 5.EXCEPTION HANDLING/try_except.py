num = int(input("Enter the number: "))
a = int(input("Enter the divisor number: "))

try:
    print(num/a)
except ZeroDivisionError:
    print("Sorry you can't divide the number by zero")

