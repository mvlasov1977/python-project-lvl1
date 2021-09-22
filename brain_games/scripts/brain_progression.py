#!/usr/bin/env python3

import brain_games.games.progression_game
from brain_games.brain_cli import execute_game


# execute calc game


def main():
    execute_game(brain_games.games.progression_game)
    return None


# detect use type


if __name__ == '__main__':
    main()
