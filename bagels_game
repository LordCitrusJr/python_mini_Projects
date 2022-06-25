# I adapted the Bagels Game from Al Sweigart's program in No Starch Press' Big Book of Small Python Projects
# This is my first program and my friend Aaron helped me out!
from random import *

# These two variables are constants. The secret number will have a no longer than the max digits.
MAX_DIGITS = 3
MAX_GUESSES = 50

# Prompts the user to play again or exits.
def exit_game():
    if not input(f'Would you like to play again? (y/n): ').startswith('y'):
        print('\nThanks for playing!\nProgram by David Wylie 2022 (My first program!)')
        exit()
    else:
        main_additional_run()  # Aditional run doesn't include welcome message function

# Provides guidance for an invalid input during the initial input function
def invalid_input(a):
    print(f'Please enter a number between 1 - {a}].')

# Provides guidance for an invalid guesses during the guess gameplay function
def invalid_guess(iis):
    print(f'Your guess must be a {iis[0]}-digit long number, try again')

# Broke out the welcome message into a function to remove it from additional plays
def welcome_message():
    print(
        '\nWelcome to the Bagels Game!\nBagels is a deductive logic game where you try to guess the '
        'Secret Number based on clues!')

# Broke out the instructions in case I need/want to change them later.
def instructions(iis):
    print(f'\nYour secret number is {iis[0]}-digits long. and you have {iis[1]} guesses to discover the secret'
          f' number.')
    print('''Try to guess what it is. Here are some clues:
        When I say:       That means:
        Pico              One digit is correct but in the wrong position.
        Fermi             One digit is correct and in the right position.
        Bagels            No digit is correct.

        For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.''')

# We get our key variables here from user inputs and return them ti iis (inital inputs).
def initial_inputs():
    # Welcome message
    num_digits = 0
    num_guesses = 0

    while True:
        nd_string = input(f'\nHow long of a secret number would you like?\nInput the number of digits you would like '
                          f'your number to be (1 - {MAX_DIGITS}): ')
        if nd_string == 'exit':
            exit_game()

        try:
            num_digits = int(nd_string)
            if num_digits > MAX_DIGITS:
                invalid_input(MAX_DIGITS)
                continue
            else:
                break
        except:
            invalid_input(MAX_DIGITS)
            continue

    while True:
        gi_string = input(
            f'\nHow many guesses would you like?\nInput the number of guesses you would like (1 - {MAX_GUESSES}): ')
        if gi_string == 'exit':
            exit_game()
        try:
            num_guesses = int(gi_string)
            if num_guesses > MAX_GUESSES:
                invalid_input(MAX_GUESSES)
                continue
            else:
                break

        except:
            invalid_input(MAX_GUESSES)
            continue
    new_tuple = (num_digits, num_guesses)  # This tuple is the info that keeps this whole thing together!
    return new_tuple

# Creates a number to guess based of our intial inputs.
def create_secret_number(iis):
    numbers = list('0123456789')
    shuffle(numbers)
    secret_number = ''
    for i in range(iis[0]):
        secret_number += str(numbers[i])
    sn = secret_number
    return sn

# This is the main gameplay loop. Runs while number of  guesses is less than user defined amount.
def guess_gameplay_loop(iis, sn):
    num_guess = 1
    while num_guess <= iis[1]:
        clues = []
        guess_input = ''
        print(f'\nGuess number {num_guess} of {iis[1]}.')
        guess_input = input(f'Please guess a {iis[0]}-digit number: ')

        if guess_input == sn:
            print(f'\nGreat Jorb! You win! The answer was {sn}')
            exit_game()

        elif len(guess_input) != iis[0]:
            invalid_guess(iis)
            continue

        elif len(guess_input) == iis[0]:
            for i in range(len(guess_input)):
                if guess_input[i] == sn[i]:
                    clues.append('Fermi')
                elif guess_input[i] in sn:
                    clues.append('Pico')

            if len(clues) == 0:
                clues.append('Bagels')
                print(f'\nHere are your clues: {clues}')
                num_guess += 1
                continue
            else:
                print(f'\nHere are your clues: {clues}')
                num_guess += 1
                continue
        else: # Through this else in here because I'm not sure if there is anything that will break this loop.
            print('Unexpected input broke the loop.')
            break
    print(f'Bad Jorb! No more guesses! You lose! The answer was {sn}.')
    exit_game()

# This is ran first time through
def main():
    welcome_message()
    iis = initial_inputs()
    instructions(iis)
    sn = create_secret_number(iis)
    guess_gameplay_loop(iis, sn)

# Additional plays remove the welcome message.
def main_additional_run():
    iis = initial_inputs()
    instructions(iis)
    sn = create_secret_number(iis)
    guess_gameplay_loop(iis, sn)

main()
