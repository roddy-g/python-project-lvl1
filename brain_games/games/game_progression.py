from brain_games.scripts import game_flow
from brain_games.scripts import gcd
import random
import prompt


def main(name):
    for _ in range(3):
        step = random.randint(1,10)
        start = random.randint(1,50)
        row = [(start + step * i) for i in range(10)]
        missing_place = random.randint(0,9)
        correct_answer = row[missing_place]
        row[missing_place] = ".."
        row_string = ' '.join([str(elem) for elem in row])
        answer = prompt.string("Question: {}\n".format(row_string))
        correct = game_flow.check(int(answer), correct_answer, name)
        if not correct:
            return False
    return True