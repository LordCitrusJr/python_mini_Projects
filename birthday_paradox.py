# Birthday Paradox Program by Al Sweigart, Python Mini Projects by No Starch Press
# Adapted by David Wylie 2022
# importing date/time and random.
import datetime
import random


# Create the birthday function with a dictionary to store month and day, randomly
def get_birthdays(num_bday_to_generate):
    birthdays = []  # Our empty list
    for i in range(num_bday_to_generate):
        starting_date = datetime.date(2020, 1, 1)  # This year is a leap year, to compare possible birthdays
        random_number_of_days = datetime.timedelta(random.randint(0, 365))
        birthday = starting_date + random_number_of_days
        birthdays.append(birthday)
    return birthdays  # This return statement will be the parameter of the next function to match.


def match_birthdays(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None  # If all birthdays are unique, return None
    for a, birthday_a in enumerate(birthdays):  # Enumerate() method adds a counter to an iterable and returns it in a
        # form of enumerating object.
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a  # Returns Birthday A (first birthday) if matched.


# Intro
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com (Adapted by David Wylie, 2022)
 
The Birthday Paradox shows us that in a group of N people, the odds 
that two of them have matching birthdays is surprisingly large. 
This program does a Monte Carlo simulation (that is, repeated random 
simulations) to explore this concept. 

(It's not actually a paradox, it's just a surprising result.)''')

# Setting up Tuples for the months
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# Get User input for number of birthdays to generate
while True:
    response = input('How many  birthdays shall I generate? (Max of 100): ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bday_to_generate = int(response)
        break  # breaks out of loop once valid input is entered.
print()

print(f'Here are {num_bday_to_generate} birthdays: ')

birthdays = get_birthdays(num_bday_to_generate)

for i, birthday in enumerate(birthdays):
    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}, '
    print(date_text, end='')
print()
print()

# Determine if two birthdays are a match
match = match_birthdays(birthdays)

# Display the results
print('In this simulation, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print(f'Multiple people have a birthday on {date_text}.')
else:
    print('There are no matching birthdays in this set.')
print()

# Run through 100,000 simulations
print(f'Generating {num_bday_to_generate} random birthdays 100,000 times...')
simulation_match = 0  # How many simulations had matching birthdays in them
for i in range(100_000):
    # Report on the progress of evry 10k simulations.
    if i % 10_000 == 0:
        print(f'{i} simulations run...')
    birthdays = get_birthdays(num_bday_to_generate)
    if match_birthdays(birthdays) != None:
        simulation_match += 1
print('100,000 simulations run')

# Display simulation results.
probability = round(simulation_match / 100_000 * 100, 2)
print(f'Out of 100,000 simulations of {num_bday_to_generate} people, there was a \n'
      f'matching birthday in that group {simulation_match} times. This means \n'
      f'that {num_bday_to_generate} people have a {probability}% chance of \n'
      f'having a matching birthday in their group.\n'
      f'That\'s probably more than you would think!!!')
