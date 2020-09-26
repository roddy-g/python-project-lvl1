from brain_games.scripts import is_prime
import random
import prompt


def main():
    number = random.randint(1, 30)
    correct_answer = is_prime.is_prime(number)
    answer = prompt.string("Question: {}\n".format(number))
    return (answer, correct_answer)
