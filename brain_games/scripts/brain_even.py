from brain_games.game_flow import play_game
from brain_games.games import even


def launch_game():
    play_game(even)


if __name__ == '__main__':
    launch_game()
