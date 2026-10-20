num = int(input("Enter the number: "))
a = int(input("Enter the divisor number: "))

try:
    print(num/a)
# except ZeroDivisionError:
except Exception as e:
    print(f"Sorry there is an exception as {e}")

else:
    print("There is no exception")

finally:
    print("It will runs, no matter what exception comes or not")

