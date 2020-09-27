import random
import prompt


def game():
    step = random.randint(1, 10)
    start = random.randint(1, 50)
    progression = [(start + step * i) for i in range(10)]
    missing_place = random.randint(0, 9)
    correct_answer = progression[missing_place]
    progression[missing_place] = ".."
    progression_string = ' '.join([str(elem) for elem in progression])
    answer = int(prompt.string("Question: {}\n".format(progression_string)))
    return (answer, correct_answer)


def print_game_task():
    print("What number is missing in the progression?\n")
