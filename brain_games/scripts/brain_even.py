#!/usr/bin/env python3

from brain_games.games.even_game import main as main_even
from brain_games.brain_cli import cli

# transwer execution to core 'cli' procedure


def main():
    cli(main_even)
    return None


# detect use type


if __name__ == '__main__':
    main()
