import random


NUMBER_LOWER_LIMIT = 1
NUMBER_UPPER_LIMIT = 100


def play():
    number_1 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    number_2 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    question = str(number_1) + ' ' + str(number_2)
    correct_answer = gcd(number_1, number_2)
    return correct_answer, question


def print_game_task():
    print("Find the greatest common divisor of given numbers.\n")


def gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 %= number_2
        else:
            number_2 %= number_1
    result = number_1 + number_2
    return result
