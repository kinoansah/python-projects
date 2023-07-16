#!/usr/bin/python3
import random

# Dictionary of words and their definitions
word_definitions = {
    'abundant': 'present in great quantity; more than adequate; oversufficient',
    'effervescent': 'vivacious; merry; lively; sparkling',
    'resilient': 'recovering readily from illness, depression, adversity, or the like',
    'serendipity': 'an aptitude for making desirable discoveries by accident',
    'zenith': 'the highest point; culmination',
    'quixotic': 'extravagantly chivalrous or romantic; visionary; impractical',
    'mellifluous': 'sweetly or smoothly flowing; sweet-sounding',
    'ephemeral': 'lasting a very short time; short-lived; transitory',
    'eloquent': 'having or exercising the power of fluent, forceful, and appropriate speech',
    'efficacious': 'capable of having the desired result or effect; effective'
}

def get_random_word():
    word = random.choice(list(word_definitions.keys()))
    definition = word_definitions[word]
    return word, definition

def display_word(word, definition):
    print("Word of the Day:", word)
    print("Definition:", definition)

def learn_new_word():
    word, definition = get_random_word()
    display_word(word, definition)

# Start the program
print("Welcome to Daily Vocabulary Booster!")
learn_new_word()

