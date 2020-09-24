from brain_games.games import game_prime
from brain_games.scripts import game_flow


def main():
    game_flow.greeting()
    print("Answer \"yes\" if number is prime. Otherwise answer \"no\".\n")
    name = game_flow.greeting_name()
    result = game_prime.main(name)
    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
