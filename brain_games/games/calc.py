import random


NUMBER_1_LOWER_LIMIT = 1
NUMBER_1_UPPER_LIMIT = 100
NUMBER_2_LOWER_LIMIT = 1
NUMBER_2_UPPER_LIMIT = 100


def generate_round():
    number_1 = random.randint(NUMBER_1_LOWER_LIMIT, NUMBER_1_UPPER_LIMIT)
    number_2 = random.randint(NUMBER_2_LOWER_LIMIT, NUMBER_2_UPPER_LIMIT)
    operation = random.choice(['+', '-', '*'])
    question = '{} {} {}'.format(number_1, operation, number_2)
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    return correct_answer, question


def print_game_task():
    print("What is the result of the expression?\n")
