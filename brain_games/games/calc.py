import random
import prompt


def main():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    answer = int(prompt.string(
        "Question: {} {} {}\n".format(number_1, operation, number_2)))
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    return(answer, correct_answer)


def print_game_task():
    print("What is the result of the expression?\n")
