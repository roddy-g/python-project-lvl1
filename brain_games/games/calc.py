import random


NUMBER_LOWER_LIMIT = 1
NUMBER_UPPER_LIMIT = 100
GAME_TASK = 'What is the result of the expression?\n'


def generate_round():
    number_1 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    number_2 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    operation = random.choice(['+', '-', '*'])
    question = '{} {} {}'.format(number_1, operation, number_2)
    if operation == '+':
        correct_answer = str(number_1 + number_2)
    elif operation == '-':
        correct_answer = str(number_1 - number_2)
    else:
        correct_answer = str(number_1 * number_2)
    return correct_answer, question
