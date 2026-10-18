sent = input("Enter the text: ")

char = 0
dig = 0
spchr = 0

for i in sent:
    if i.isdigit():
        dig = dig + 1
    elif i.isalpha():
        char = char + 1
    else:
        spchr = spchr + 1

print(f"Number of digits are: {dig}\nNumber of characters are: {char} and \nNumber of Special characters are: {spchr}")