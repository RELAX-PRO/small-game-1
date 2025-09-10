"""guess the number"""
import random
print("Welcome the number guessing game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
# print(f"Psst, the correct answer is {number}")
attempt = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if attempt == 'easy':
    attempts = 10
elif attempt == 'hard':
    attempts = 5
else:
    print("Invalid input")
while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess > number:
        print("Too high")
        print(f"You have {attempts - 1} attempts remaining to guess the number.")
    elif guess < number:
        print("Too low")
        print(f"You have {attempts - 1} attempts remaining to guess the number.")
    if attempts == 0:
        print("You've run out of guesses, you lose.")
    attempts -= 1