from brain_games.games import game_gcd
from brain_games.scripts import game_flow


def main():
    game_flow.greeting()
    print("Find the greatest common divisor of given numbers.")
    name = game_flow.greeting_name()
    result = game_gcd.main(name)
    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
