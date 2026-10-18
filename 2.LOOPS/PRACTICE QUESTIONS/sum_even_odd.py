num = int(input("Enter the number: "))

even = 0
odd = 0
for i in range(1,num+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print(f"Even sum is: {even} and Odd sum is: {odd}")