from brain_games.game_engine import game_flow
from brain_games.games import prime


def play_game():
    game_flow.game_loop(prime)


if __name__ == '__main__':
    play_game()
