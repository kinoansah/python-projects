#!/usr/bin/python3
# Points assigned to each letter
letter_points = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def calculate_score(word):
    score = 0
    for letter in word:
        letter = letter.lower()
        score += letter_points.get(letter, 0)
    return score

def play_scrabble():
    word = input("Enter a word: ")
    score = calculate_score(word)

    print("Word:", word)
    print("Score:", score)

# Start the game
play_scrabble()

