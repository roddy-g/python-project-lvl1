from brain_games.game_engine import gcd
import random


def play():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = str(number_1) + ' ' + str(number_2)
    correct_answer = gcd.gcd(number_1, number_2)
    return correct_answer, question


def print_game_task():
    print("Find the greatest common divisor of given numbers.\n")
