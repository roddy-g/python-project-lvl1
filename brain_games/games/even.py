import random


NUMBER_LOWER_LIMIT = 1
NUMBER_UPPER_LIMIT = 100
GAME_TASK = 'Answer "yes" if number even otherwise answer "no".\n'


def generate_round():
    number = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
