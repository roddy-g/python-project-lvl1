from brain_games.scripts import game_flow
from brain_games.games import game_calc


def main():
    game_flow.game_cycle(game_calc)


if __name__ == '__main__':
    main()
