from brain_games.game_engine import is_prime
import random


def play():
    number = random.randint(1, 30)
    if is_prime.is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def print_game_task():
    print("Answer \"yes\" if number is prime. Otherwise answer \"no\".\n")
