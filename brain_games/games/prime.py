import random


NUMBER_LOWER_LIMIT = 1
NUMBER_UPPER_LIMIT = 30
GAME_TASK = 'Answer "yes" if number is prime. Otherwise answer "no".\n'


def generate_round():
    number = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if (number % i) == 0:
            return False
    return True
