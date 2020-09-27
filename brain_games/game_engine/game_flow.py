import prompt


game_cycles_count = 3


def get_name_and_greet():
    user_name = prompt.string('May I have your name? ')
    print('Hello, ', user_name, "!\n")
    return user_name


def game_loop(game):
    print("\nWelcome to the Brain Games!")
    game.print_game_task()
    user_name = get_name_and_greet()
    for _ in range(game_cycles_count):
        answer, correct_answer = game.main()
        if answer == correct_answer:
            print('Correct!')
        else:
            print("""\"{}\" is wrong answer ;(. Correct answer was \"{}\".
Let\"s try again, {}!""".format(answer, correct_answer, user_name))
            return False
    print('Congratulations, {}!'.format(user_name))
