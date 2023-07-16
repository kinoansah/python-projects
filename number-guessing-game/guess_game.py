#!/usr/bin/python3
import random

def play_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    guess_limit = 3
    guesses_taken = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10. Can you guess it?")

    while guesses_taken < guess_limit:
        # Get user input
        guess = input("Take a guess: ")

        # Validate the input
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 10:
            print("Invalid guess! Please enter a number between 1 and 10.")
            continue

        guesses_taken += 1
        guess = int(guess)

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    # If the player couldn't guess the number within the guess limit
    if guesses_taken == guess_limit:
        print("Sorry, you couldn't guess the number. The number was", secret_number)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")

# Start the game
play_game()
