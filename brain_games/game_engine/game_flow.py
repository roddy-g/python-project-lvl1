import prompt


NUMBER_OF_GAME_CYCLES = 3


def get_name_and_greet():
    user_name = prompt.string('May I have your name? ')
    print('Hello, ', user_name, "!\n")
    return user_name


def play_game(game):
    print("\nWelcome to the Brain Games!")
    print(game.GAME_TASK)
    user_name = get_name_and_greet()
    for _ in range(NUMBER_OF_GAME_CYCLES):
        correct_answer, question = game.generate_round()
        answer = prompt.string("Question: {}\n".format(question))
        if answer == correct_answer:
            print('Correct!')
            all_anwers_were_correct = True
        else:
            print('\"{}\" is wrong answer ;(. '.format(answer), end='')
            print('Correct answer was \"{}\"'.format(correct_answer))
            print('Let\"s try again, {}!'.format(user_name))
            all_anwers_were_correct = False
            break
    if all_anwers_were_correct:
        print('Congratulations, {}!'.format(user_name))
