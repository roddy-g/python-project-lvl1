from brain_games.game_engine import game_flow
from brain_games.games import gcd


def play_game():
    game_flow.game_loop(gcd)


if __name__ == '__main__':
    play_game()
