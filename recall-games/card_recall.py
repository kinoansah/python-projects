#!/usr/bin/python3
import random
import os

# Function to create a shuffled deck of cards
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Function to ask the user to recall the cards in order
def recall_cards(deck):
    score = 0
    for card in deck:
        rank, suit = card
        user_input = input("Recall the next card: ")
        if user_input.lower() == rank.lower() + " of " + suit.lower():
            score += 1
        else:
            break
    return score

# Main program
print("Welcome to the Card Recall Game!")
print("You will be shown a shuffled deck of cards and need to recall them in order.")

# Create and shuffle the deck
deck = create_deck()

# Display the shuffled deck
print("Shuffled Deck:")
for card in deck:
    rank, suit = card
    print(rank, "of", suit)

# Wait for user to finish memorizing the deck
input("Press Enter when you are ready to recall the cards...")

# Clear the console screen
os.system("clear")  # For Linux/Mac
# os.system("cls")  # For Windows

# Ask the user to recall the cards
score = recall_cards(deck)

# Print the score
print("Your score:", score, "/ 52")
