import random
import os

# get player number 5 times


def get_players_number():
    try:
        number_input = input(
            'Enter your 5 numbers, between 1 and 20, separated by space,' +
            '\nOr type "exit" or "q" to quit: ')
        number_list = number_input.split(' ')
        exitText = number_input.strip()
        false_check = False
        if exitText == 'exit' or exitText == 'q':
            os._exit(1)
        for num in number_list:
            num = int(num)
            if num < 1 or num > 20:
                print('number {} is not between 1 and 20'.format(num))
                false_check = True
        if false_check:
            return
        integer_set = {int(number) for number in number_list}
        if len(integer_set) != 5:
            return print('Enter only 5 numbers I said...')
        return integer_set
    except ValueError:
        print('Enter numbers (with commas), dumbass :/')

# lottery calculates 5 random numbers (between 1 and 20)


def create_lottery_numbers():
    values = set()
    while len(values) < 5:
        values.add(random.randint(1, 20))
    return values


def menu():
    try:
        user_numbers = get_players_number()
        lottery_numbers = create_lottery_numbers()
        # using magic of set to match
        matched_numbers = user_numbers.intersection(lottery_numbers)
        if len(matched_numbers) is 0:
            return print('No match. Better luck next time :)')
        print('You matched {}. You won ${}! Congrats, you bastard :)'.format(
            matched_numbers, 1000 * len(matched_numbers)))
    except AttributeError:
        print('You did something wrong with input. Is it that hard?')
        menu()


# start
menu()
