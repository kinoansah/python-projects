#!/usr/bin/python3
import random
import os

def create_deck():
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def omit_cards(deck, num_omitted):
    omitted_cards = []
    for _ in range(num_omitted):
        card = deck.pop()
        omitted_cards.append(card)
    return omitted_cards

def get_missing_cards(omitted_cards):
    missing_cards = []
    for i in range(1, 6):
        card = input(f"Enter missing card #{i}: ")
        missing_cards.append(card)
    return missing_cards

def calculate_score(omitted_cards, missing_cards):
    correct_answers = [card for card in missing_cards if card in omitted_cards]
    score = len(correct_answers)
    return score

def main():
    deck = create_deck()
    omitted_cards = omit_cards(deck, 5)

    print("Remaining 47 shuffled cards:")
    for card in deck:
        print(f"{card[0]} of {card[1]}")

    input("Press Enter to name the missing cards...")
    os.system('cls' if os.name == 'nt' else 'clear')

    missing_cards = get_missing_cards(omitted_cards)

    print("\nThe missing cards were:")
    for card in omitted_cards:
        print(f"{card[0]} of {card[1]}")

    missing_cards.sort(key=lambda x: x in omitted_cards, reverse=True)
    score = calculate_score(omitted_cards, missing_cards)

    print("\nYour cards were:")
    for card in missing_cards:
        print(card)

    print(f"\nScore: {score}/5")

if __name__ == "__main__":
    main()
