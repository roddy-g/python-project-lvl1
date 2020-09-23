from brain_games.scripts import game_flow
import prompt
import random


def main():
    game()


def game():
    game_flow.greeting()
    print("Answer \"yes\" if number even otherwise answer \"no\".\n")
    name = game_flow.greeting_name()
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
    print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
