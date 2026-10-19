def pallindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]
    print(rev)
    if rev == st:
        print("Pallindrome")
    else:
        print("Not a Pallindrome")

pallindrome("malayalam")