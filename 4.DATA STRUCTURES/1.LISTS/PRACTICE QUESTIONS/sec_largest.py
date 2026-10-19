l = [65,34,32,87,67,56,68,78]

largest = l[0]
second_largest = l[0]

for i in l:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i
print(second_largest, largest)