from brain_games.games import game_progression
from brain_games.scripts import game_flow


def main():
    game_flow.greeting()
    print("What number is missing in the progression?")
    name = game_flow.greeting_name()
    result = game_progression.main(name)
    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
