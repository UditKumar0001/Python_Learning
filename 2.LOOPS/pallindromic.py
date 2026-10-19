num = int(input("Enter the number: "))

orig = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print("Reversed Number is: ",rev)
if rev == orig:
    print(f"{orig} is a pallindromic number")
else:
    print(f"{orig} is not a pallindromic number")

