import prompt


NUMBER_OF_GAME_ROUNDS = 3


def get_name_and_greet():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(user_name))
    return user_name


def play_game(game):
    print("\nWelcome to the Brain Games!")
    print(game.GAME_TASK)
    user_name = get_name_and_greet()
    for round_ in range(NUMBER_OF_GAME_ROUNDS):
        correct_answer, question = game.generate_round()
        answer = prompt.string("Question: {}\n".format(question))
        if answer == correct_answer:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. '.format(answer), end='')
            print('Correct answer was "{}"'.format(correct_answer))
            print('Let"s try again, {}!'.format(user_name))
            break
    else:
        print('Congratulations, {}!'.format(user_name))
