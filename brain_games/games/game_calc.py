import random
import prompt


def main():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operations_list = ['+', '-', '*']
    operation = random.choice(operations_list)
    answer = int(prompt.string(
        "Question: {} {} {}\n".format(number_1, operation, number_2)))
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    return(answer, correct_answer)
