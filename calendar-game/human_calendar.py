#!/usr/bin/python3
import datetime
import random

def generate_random_date():
    start_date = datetime.date(1752, 1, 1)
    end_date = datetime.date(2100, 12, 31)
    random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date

def get_day_of_week(date):
    day_of_week = date.strftime("%A")
    return day_of_week

def format_date(date):
    formatted_date = date.strftime("%B %d, %Y")
    return formatted_date

def get_full_day_name(abbreviated_day):
    days = {
        'm': 'Monday',
        'tu': 'Tuesday',
        'w': 'Wednesday',
        'th': 'Thursday',
        'f': 'Friday',
        'sa': 'Saturday',
        'su': 'Sunday'
    }
    return days.get(abbreviated_day.lower())

def main():
    while True:
        score = 0
        for i in range(10):
            random_date = generate_random_date()
            date_str = format_date(random_date)

            print("Determine the day of the week for the following date:")
            print(date_str)

            user_input = input("Enter the day of the week: ")

            if not user_input:
                print("Please enter at least one character.")
                continue

            # Check if the user input matches the starting letter of any day
            matching_days = [day for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] if day.startswith(user_input.lower())]

            if len(matching_days) == 1:
                user_input = matching_days[0][:len(user_input)]  # Auto-complete the day of the week

            expected_day_of_week = get_day_of_week(random_date)

            if user_input.lower() == expected_day_of_week.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct day of the week is {expected_day_of_week}.")

        print(f"Your score is: {score} out of 10")

        play_again = input("Play another round? (Y/N): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()

