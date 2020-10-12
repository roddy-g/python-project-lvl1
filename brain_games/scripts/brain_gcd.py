from brain_games.games.game_flow import play_game
from brain_games.games import gcd


def launch_game():
    play_game(gcd)


if __name__ == '__main__':
    launch_game()
