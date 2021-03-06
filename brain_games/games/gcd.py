import random


NUMBER_LOWER_LIMIT = 1
NUMBER_UPPER_LIMIT = 100
GAME_TASK = 'Find the greatest common divisor of given numbers.'


def generate_round():
    number_1 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    number_2 = random.randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    question = '{} {}'.format(number_1, number_2)
    correct_answer = str(find_gcd(number_1, number_2))
    return correct_answer, question


def find_gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 %= number_2
        else:
            number_2 %= number_1
    result = number_1 + number_2
    return result
