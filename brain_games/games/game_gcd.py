from brain_games.scripts import game_flow
from brain_games.scripts import gcd
import random
import prompt


def main(name):
    for _ in range(3):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        answer = prompt.string(
            "Question: {} {}\n".format(number_1, number_2))
        correct_answer = gcd.gcd(number_1, number_2)
        correct = game_flow.check(int(answer), correct_answer, name)
        if not correct:
            return False
    return True
