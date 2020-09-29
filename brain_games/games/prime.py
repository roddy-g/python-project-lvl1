import random


NUMBER_LOWER_LIMIT = 1
NUMBER_UPPER_LIMIT = 30


def play():
    number = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def print_game_task():
    print("Answer \"yes\" if number is prime. Otherwise answer \"no\".\n")


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
    else:
        return False
    return True
