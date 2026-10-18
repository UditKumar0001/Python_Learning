text = input("Enter the sentence which you wants to reverse it: ")

reverse = ""
for i in range(len(text)-1,-1,-1):
    reverse = reverse + text[i]

if reverse == text:
    print(f"{text} is a Pallindrome")

else:
    print(f"{text} is not a Pallindrome")