l = [34,23,45,12,19,98]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] >= largest:
        largest = l[i]
        index = i
print(f"Largest number is: {largest}\nIndex of the largest number is: {index}")
    
        
