#!/usr/bin/env python3

from random import randint
from brain_games.brain_cli import cli

_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# initial parameters section

_RANDOM_RANGE = (1, 100)  # rand fst number for randint function
_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers


# generate a random number

def get_random_int(range):
    begin, end = range
    return randint(begin, end)


# main number

def main_number(a):
    if a >= 2:
        subsequence = range(2, a - 1)
        for x in subsequence:
            if a % x == 0:
                return 'no'
        else:
            return 'yes'
    else:
        return 'no'


# create full sentence

def get_full_sentence(a):
    s = []
    s.append(str(a))
    s.append(main_number(a))
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
