a = [300,300,400,300,400,500,600,800,900,200,400,600]

d = {}
for i in a:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)