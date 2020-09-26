from brain_games.games import game_prime
from brain_games.scripts import game_flow


def main():
    game_flow.game_cycle(game_prime)


if __name__ == '__main__':
    main()
