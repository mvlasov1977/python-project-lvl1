#!/usr/bin/env python3

from random import randint
from brain_games.brain_cli import cli

_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


# initial parameters section


_RANDOM_RANGE = (1, 10)  # randomise range for randint function
_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers


# generate a random number


def get_random_int(range):
    begin, end = range
    return randint(begin, end)


# parity check


def parity_chk(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


# create full sentence


def get_full_sentence(a):
    s = []
    s.append(a)
    s.append(parity_chk(a))
    return s


# define function main


def main():
    item_count = 0
    s = []
    while item_count < _NUM_OF_CORR_ANSWERS:
        a = get_random_int(_RANDOM_RANGE)
        s.append(get_full_sentence(a))
        item_count += 1
    cli(s, _RULE)
    return None


# detect use type


if __name__ == '__main__':
    main()
