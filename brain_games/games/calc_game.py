#!/usr/bin/env python3

from random import randint, choice
from brain_games.brain_cli import cli

_RULE = 'What is the result of the expression?'


# initial parameters section


_RANDOM_RANGE = (1, 10)  # randomise range for randint function
_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers
_OPERATION = ['+', '-', '*']


# generate a random number


def get_random_int(range):
    begin, end = range
    return randint(begin, end)


# generate operation


def get_random_operation(range):
    return choice(range)


# create full sentence


def get_full_sentence(a, b, operation):
    s = []
    s.append(str(a) + operation + str(b))
    if operation == '+':
        s.append(str(a + b))
        return s
    elif operation == '-':
        s.append(str(a - b))
        return s
    elif operation == '*':
        s.append(str(a * b))
        return s
    else:
        return None  # generate exception


# define function main


def main():
    item_count = 0
    s = []
    while item_count < _NUM_OF_CORR_ANSWERS:
        a = get_random_int(_RANDOM_RANGE)
        b = get_random_int(_RANDOM_RANGE)
        o = get_random_operation(_OPERATION)
        s.append(get_full_sentence(a, b, o))
        item_count += 1
    cli(s, _RULE)
    return None


# detect use type


if __name__ == '__main__':
    main()
