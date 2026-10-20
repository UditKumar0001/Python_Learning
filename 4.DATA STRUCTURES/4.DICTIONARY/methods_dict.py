d = {10: 100, 20: 200, 30: 300, 40: 400}

# d.clear()
b = d.copy() # shallow copy, if .copy is not considered, then it will be a deep copy
d[50] = 500
# print(b)
print(d.items())