from brain_games.scripts import game_flow
import prompt
import random


def main(name):
    for _ in range(3):
        number = random.randint(1, 100)
        answer = prompt.string("Question: {}\n".format(number))
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        correct = game_flow.check(answer, correct_answer, name)
        if not correct:
            return False
    return True
