#!/usr/bin/env python3

from brain_games.games.gcd_game import main as main_gcd
from brain_games.brain_cli import cli


# transwer execution to core 'cli' procedure

def main():
    cli(main_gcd)
    return None


# detect use type


if __name__ == '__main__':
    main()
