import random

def release_stress():
    """This function helps the user release stress."""
    # Generate a random number between 1 and 5.
    number = random.randint(1, 5)

    # Based on the random number, print a message to help the user release stress.
    if number == 1:
        print("Take a deep breath and count to 10.")
    elif number == 2:
        print("Go for a walk or do some other form of exercise.")
    elif number == 3:
        print("Listen to some calming music.")
    elif number == 4:
        print("Spend time with loved ones.")
    else:
        print("Do something you enjoy.")

if __name__ == "__main__":
  release_stress()
