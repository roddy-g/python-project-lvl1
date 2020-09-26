from brain_games.scripts import game_flow
from brain_games.games import game_even


def main():
    game_flow.game_cycle(game_even)


if __name__ == '__main__':
    main()
