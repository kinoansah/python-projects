#!/usr/bin/python3
import random

def generate_secret_word():
    word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'mango', 'peach']
    return random.choice(word_list)

def get_guess():
    guess = input("Enter your guess (5-letter word): ")
    return guess.lower()

def check_guess(secret_word, guess):
    if len(guess) != 5:
        return False

    correct_letters = 0
    correct_positions = 0

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            correct_positions += 1
        elif guess[i] in secret_word:
            correct_letters += 1

    print("Correct letters:", correct_letters)
    print("Correct positions:", correct_positions)

    if correct_positions == 5:
        return True
    else:
        return False

def play_wordle():
    secret_word = generate_secret_word()
    attempts = 0
    max_attempts = 10

    print("Welcome to Wordle!")
    print("Try to guess the secret 5-letter word. You have", max_attempts, "attempts.")

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        if check_guess(secret_word, guess):
            print("Congratulations! You guessed the word in", attempts, "attempts.")
            break
        else:
            print("Incorrect guess. Please try again.")

    if attempts == max_attempts:
        print("Sorry, you ran out of attempts. The secret word was:", secret_word)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_wordle()
    else:
        print("Thank you for playing Wordle!")

# Start the game
play_wordle()
