def Addition(*args):
    sum = 0
    for i in args:
        sum = sum + i

    print(sum)

Addition(32, 45, 67, 89, -0, 43, -9)