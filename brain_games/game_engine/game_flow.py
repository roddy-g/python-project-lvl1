import prompt


NUMBER_OF_GAME_CYCLES = 3


def get_name_and_greet():
    user_name = prompt.string('May I have your name? ')
    print('Hello, ', user_name, "!\n")
    return user_name


def game_loop(game):
    print("\nWelcome to the Brain Games!")
    game.print_game_task()
    user_name = get_name_and_greet()
    for _ in range(NUMBER_OF_GAME_CYCLES):
        correct_answer, question = game.play()
        answer = prompt.string("Question: {}\n".format(question))
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print('\"{}\" is wrong answer ;(. '.format(answer), end='')
            print('Correct answer was \"{}\"'.format(correct_answer))
            print('Let\"s try again, {}!'.format(user_name))
            return False
    print('Congratulations, {}!'.format(user_name))
