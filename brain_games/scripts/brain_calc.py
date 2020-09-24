from brain_games.scripts import game_flow
from brain_games.games import game_calc


def main():
    game_flow.greeting()
    print("What is the result of the expression?\n")
    name = game_flow.greeting_name()
    result = game_calc.main(name)
    if result:
        print("Congratulations,  {}!".format(name))


if __name__ == '__main__':
    main()
