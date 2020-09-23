from brain_games.scripts import game_flow
from brain_games.games import game_even
import random
import prompt


def main():
    game_flow.greeting()
    print("Answer \"yes\" if number even otherwise answer \"no\".\n")
    name = game_flow.greeting_name()
    result = game_even.main(name)
    if result:
    	print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()