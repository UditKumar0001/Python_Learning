num = int(input("Enter the number for which you wants to calculate the factorial: "))

sum = 1
if num == 0 or num == 1:
    print(1)

for i in range(1,num+1):
    sum = sum * i
print(sum)