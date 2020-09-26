import random
import prompt


def main():
    step = random.randint(1, 10)
    start = random.randint(1, 50)
    row = [(start + step * i) for i in range(10)]
    missing_place = random.randint(0, 9)
    correct_answer = row[missing_place]
    row[missing_place] = ".."
    row_string = ' '.join([str(elem) for elem in row])
    answer = int(prompt.string("Question: {}\n".format(row_string)))
    return (answer, correct_answer)
