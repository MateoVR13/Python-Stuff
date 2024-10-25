import random

randNum = random.randint(1, 100)


while True:
    guess = int(input("\nEnter a number: "))
    
    if guess == randNum:
        print("\nCongratulations! You guessed the number!")
        break
    elif guess < randNum:
        print("\nThe number is too low.")
        print("Try again!")
    else:
        print("\nThe number is too high.")
        print("Try again!")
        