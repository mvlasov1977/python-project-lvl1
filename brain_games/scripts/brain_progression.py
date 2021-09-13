#!/usr/bin/env python3

from brain_games.games.progression_game import main as main_progression
from brain_games.brain_cli import cli


# execute calc game


def main():
    cli(main_progression)
    return None


# detect use type


if __name__ == '__main__':
    main()
