import prompt


NUMBER_OF_GAME_ROUNDS = 3


def play_game(game):
    print("\nWelcome to the Brain Games!")
    print(game.GAME_TASK, end='\n')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(user_name))
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
