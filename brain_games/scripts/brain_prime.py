#!/usr/bin/env python3

from brain_games.games.prime_game import main as main_prime
from brain_games.brain_cli import cli


# transwer execution to core 'cli' procedure

def main():
    cli(main_prime)
    return None


# detect use type


if __name__ == '__main__':
    main()
