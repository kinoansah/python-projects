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

def main():
    random_date = generate_random_date()
    date_str = format_date(random_date)

    print("Determine the day of the week for the following date:")
    print(date_str)

    user_input = input("Enter the day of the week: ")
    expected_day_of_week = get_day_of_week(random_date)

    if user_input.lower() == expected_day_of_week.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct day of the week is {expected_day_of_week}.")

if __name__ == "__main__":
    main()
