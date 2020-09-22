import prompt
import random


def main():
    game()


def game():
    print("""Welcome to the Brain Games!\nAnswer \"yes\"
     if number even otherwise answer \"no\".\n""")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, "!\n")
    for _ in range(3):
        number = random.randint(1, 100)
        answer = prompt.string("Question: {}\n".format(number))
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print("""\"{}\" is wrong answer ;(. Correct answer was
        \"{}\".\nLet\"s try again, {}!""".format(answer, correct_answer, name))
            return False
    print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
