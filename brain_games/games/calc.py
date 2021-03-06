import random


NUMBER_LOWER_LIMIT = 1
NUMBER_UPPER_LIMIT = 100
GAME_TASK = 'What is the result of the expression?'


def generate_round():
    number_1 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    number_2 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    operation = random.choice(['+', '-', '*'])
    question = '{} {} {}'.format(number_1, operation, number_2)
    correct_answer = str(apply_operation(number_1, number_2, operation))
    return correct_answer, question


def apply_operation(number_1, number_2, operation):
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    elif operation == '*':
        correct_answer = number_1 * number_2
    else:
        raise ValueError('Operation "{}" is not defined!!'.format(operation))
    return correct_answer
