import prompt
import random


def main():
    number = random.randint(1, 100)
    answer = prompt.string("Question: {}\n".format(number))
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return(answer, correct_answer)


def print_game_task():
    print("Answer \"yes\" if number even otherwise answer \"no\".\n")
