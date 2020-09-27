import random


def play():
    number = random.randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def print_game_task():
    print("Answer \"yes\" if number even otherwise answer \"no\".\n")
