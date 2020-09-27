from brain_games.scripts import gcd
import random
import prompt


def main():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    answer = int(prompt.string(
        "Question: {} {}\n".format(number_1, number_2)))
    correct_answer = gcd.gcd(number_1, number_2)
    return (answer, correct_answer)


def print_game_task():
    print("Find the greatest common divisor of given numbers.\n")
