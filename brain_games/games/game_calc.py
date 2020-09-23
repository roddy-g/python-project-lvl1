from brain_games.scripts import game_flow
import random
import prompt


def main(name):
    for _ in range(3):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        operations_list = ['+', '-', '*']
        operation = random.choice(operations_list)
        answer = prompt.string(
            "Question: {} {} {}\n".format(number_1, operation, number_2))
        if operation == '+':
            correct_answer = number_1 + number_2
        elif operation == '-':
            correct_answer = number_1 - number_2
        else:
            correct_answer = number_1 * number_2
        correct = game_flow.check(int(answer), correct_answer, name)
        if not correct:
            return False
    return True
