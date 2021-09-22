#!/usr/bin/env python3

import brain_games.games.even_game
from brain_games.brain_cli import execute_game

# transwer execution to core 'cli' procedure


def main():
    execute_game(brain_games.games.even_game)
    return None


# detect use type


if __name__ == '__main__':
    main()
