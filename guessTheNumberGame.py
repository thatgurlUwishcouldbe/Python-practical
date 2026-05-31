import random

secretNumber = random.randint(1, 10)
attempts = 0

print("Guess The Number Game")
print("Guess a number from 1 to 10")

while True:

    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secretNumber:
        print("Higher")

    elif guess > secretNumber:
        print("Lower")

    else:
        print("Congratulations! You guessed the correct number")
        print("Number of attempts:", attempts)
        break
