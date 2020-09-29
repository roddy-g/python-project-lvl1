from brain_games.game_engine.game_flow import play_game
from brain_games.games import prime


def launch_game():
    play_game(prime)


if __name__ == '__main__':
    launch_game()
