#!/usr/bin/python3
import random

# List of words for the puzzle
words = ["apple", "banana", "cherry", "grape", "orange", "mango", "peach"]

def generate_puzzle(words):
    # Select a random word from the list
    word = random.choice(words)

    # Create a list of shuffled letters
    letters = list(word)
    random.shuffle(letters)

    return word, letters

def display_puzzle(letters):
    print("Word Puzzle:")
    print(" ".join(letters))

def check_solution(word, guess):
    if word == guess:
        return True
    else:
        return False

def play_word_puzzle():
    word, letters = generate_puzzle(words)
    attempts = 0
    max_attempts = 3

    print("Welcome to the Word Puzzle!")
    print("Rearrange the letters to form a word.")

    while attempts < max_attempts:
        display_puzzle(letters)

        guess = input("Enter your guess: ")

        if check_solution(word, guess):
            print("Congratulations! You solved the puzzle!")
            break
        else:
            attempts += 1
            print("Incorrect guess. Please try again.")

    if attempts == max_attempts:
        print("Sorry, you ran out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_word_puzzle()
    else:
        print("Thank you for playing Word Puzzle!")

# Start the game
play_word_puzzle()

