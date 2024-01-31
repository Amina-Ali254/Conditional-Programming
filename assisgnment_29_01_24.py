# Write a program to convert seconds into hours, minutes, and seconds?

def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds
total_seconds = int(input("Enter the number of seconds: "))
hours, minutes, seconds = convert_seconds(total_seconds)
print("{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

# Write a program to determine if a given number is positive, negative, or zero?

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
number = float(input("Enter a number: "))
result = check_number(number)
print("The number is {result}.")

# Write a program to check if a given character is a vowel or a consonant?

def check_character(char):
    vowels = 'aeiouAEIOU'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char in letters:
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not a letter"
character = input("Enter a character: ")
if len(character) == 1:
    result = check_character(character)
    print(f"The character '{character}' is a {result}.")
else:
    print("Please enter a single character.")

# Write a program to check if a given year is a leap year?

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Write a python program to check if a year is a century year or not.
    
def is_century_year(year):
    if year % 100 == 0:
        return True
    else:
        return False
year = int(input("Enter a year: "))
if is_century_year(year):
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")

# Write a python program to determine eligibility for voting based on age.
    
def is_eligible_for_voting(age):
    minimum_voting_age = 18
    if age >= minimum_voting_age:
        return True
    else:
        return False
age = int(input("Enter your age: "))
if is_eligible_for_voting(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Write a python program to determine the season based on the month?

def determine_season_in_kenya(month):
    seasons = {
        'January': 'Dry', 'February': 'Dry',
        'March': 'Long Rains', 'April': 'Long Rains', 'May': 'Long Rains',
        'June': 'Dry', 'July': 'Dry', 'August': 'Dry', 
        'September': 'Dry', 'October': 'Short Rains',
        'November': 'Short Rains', 'December': 'Short Rains',
        1: 'Dry', 2: 'Dry', 3: 'Long Rains', 4: 'Long Rains', 5: 'Long Rains',
        6: 'Dry', 7: 'Dry', 8: 'Dry', 9: 'Dry', 10: 'Short Rains',
        11: 'Short Rains', 12: 'Short Rains'}
    if isinstance(month, str):
        month = month.title()
    return seasons.get(month, "Invalid month")
month_input = input("Enter the month (name or number): ")
try:
    month_input = int(month_input)
except ValueError:
    pass
season = determine_season_in_kenya(month_input)
print(f"The season in Kenya during {month_input} is: {season}.")
