#!/usr/bin/python3
def play_hangaroo():
    secret_word = "hangaroo"
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangaroo!")
    print("Guess the letters to reveal the secret word.")

    while attempts < max_attempts:
        print("\nSecret word:", end=" ")
        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        guess = input("\n\nEnter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("Correct guess!")
            else:
                attempts += 1
                print("Incorrect guess. You have", max_attempts - attempts, "attempt(s) left.")
        else:
            print("Invalid input. Please enter a single letter.")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word correctly:", secret_word)
            break

    if attempts == max_attempts:
        print("\nSorry, you ran out of attempts. The secret word was:", secret_word)

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_hangaroo()
    else:
        print("\nThank you for playing Hangaroo!")

# Start the game
play_hangaroo()
