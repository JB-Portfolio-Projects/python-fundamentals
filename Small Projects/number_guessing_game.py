#random generaration, with a selected number for guessing
import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#generate number and have the user guess. add v1.1. Input validation, quit option, and guess counter.
attempts = 0
while True:
        user_input = input("Enter your guess (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
                break
        else:
            print("Invalid input. Please enter a number.")