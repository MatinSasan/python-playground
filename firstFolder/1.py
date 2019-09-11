import random

magic_number = [random.randint(0, 9), random.randint(0, 9)]


def ask_user_and_check_number():
    input_data = input('Enter a number between 0 and 9: ')
    if input_data == '':
        print('why no input?!')
        return
    try:
        user_number = int(input_data)
    except ValueError:
        print('Use numbers')
        return
    if 0 > user_number or user_number > 9:
        print('I said between 0 and 9, dumbass')
        return
    if user_number in magic_number:
        print('lucky fucker :)')
    if user_number not in magic_number:
        print('that sucks :/')


chances = 3


def run_progam_x_times():
    for attempt in range(chances):
        print("this is attempt {}".format(attempt))
        ask_user_and_check_number()


run_progam_x_times()
