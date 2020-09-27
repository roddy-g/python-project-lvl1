import random


def play():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = str(number_1) + operation + str(number_2)
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    return correct_answer, question


def print_game_task():
    print("What is the result of the expression?\n")
