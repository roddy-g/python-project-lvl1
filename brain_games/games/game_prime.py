from brain_games.scripts import game_flow
from brain_games.scripts import is_prime
import random
import prompt


def main(name):
    for _ in range(3):
        number = random.randint(1, 30)
        correct_answer = is_prime.is_prime(number)
        answer = prompt.string("Question: {}\n".format(number))
        correct = game_flow.check(answer, correct_answer, name)
        if not correct:
            return False
    return True
