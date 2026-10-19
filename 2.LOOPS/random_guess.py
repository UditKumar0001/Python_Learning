import random

num = random.randint(1, 10)

tries = 0

while True:
    guess = int(input("Please guess the number between  1 to 10: "))

    if guess == num:
        tries = tries + 1
        print(f"Hurraa! You are a computer mind reader, you guessed the number in {tries} tries")
        break
    elif guess > num:
        tries =tries + 1
        print("Go a little lower")
    elif guess < num:
        tries = tries + 1
        print("Go a little higher")
    else:
        tries = tries + 1
        print("Better luck next time")