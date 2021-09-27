#!/usr/bin/env python3

import brain_games.games.gcd_game
from brain_games.brain_games_core import execute_game


# transwer execution to core 'cli' procedure

def main():
    execute_game(brain_games.games.gcd_game)
    return None


# detect use type


if __name__ == '__main__':
    main()
