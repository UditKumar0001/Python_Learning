num = int(input("Enter the number for checking it's prime or not: "))

count = 0
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
        
   