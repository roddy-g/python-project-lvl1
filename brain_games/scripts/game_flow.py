from brain_games.games import game_even
from brain_games.games import game_calc
from brain_games.games import game_gcd
from brain_games.games import game_prime
from brain_games.games import game_progression
import prompt


def greeting(game_type):
    print("\nWelcome to the Brain Games!")
    if game_type == game_even:
        print("Answer \"yes\" if number even otherwise answer \"no\".\n")
    elif game_type == game_calc:
        print("What is the result of the expression?\n")
    elif game_type == game_gcd:
        print("Find the greatest common divisor of given numbers.\n")
    elif game_type == game_progression:
        print("What number is missing in the progression?\n")
    elif game_type == game_prime:
        print("Answer \"yes\" if number is prime. Otherwise answer \"no\".\n")


def get_name():
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, "!\n")
    return name


def game_cycle(game_type):
    greeting(game_type)
    name = get_name()
    for _ in range(3):
        answer, correct_answer = game_type.main()
        if answer == correct_answer:
            print('Correct!')
        else:
            print("""\"{}\" is wrong answer ;(. Correct answer was \"{}\".
Let\"s try again, {}!""".format(answer, correct_answer, name))
            return False
