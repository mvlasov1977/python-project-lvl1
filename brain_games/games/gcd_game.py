#!/usr/bin/env python3

from random import randint
from brain_games.brain_cli import cli

_RULE = 'Find the greatest common divisor of given numbers.'


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


# gcd calculation (binary Evklid algorythm)

def gcd_calculation(a, b):
    if a == 0 and b != 0:
        result = b
    elif a != 0 and b == 0:
        result = a
    elif a == b:
        result = a
    elif a == 1 or b == 1:
        result = 1
    elif parity_chk(a) == 'yes' and parity_chk(b) == 'yes':
        result = 2 * gcd_calculation(a / 2, b / 2)
    elif parity_chk(a) == 'yes' and parity_chk(b) == 'no':
        result = gcd_calculation(a / 2, b)
    elif parity_chk(a) == 'no' and parity_chk(b) == 'yes':
        result = gcd_calculation(a, b / 2)
    elif a < b:
        result = gcd_calculation((b - a) / 2, a)
    elif a > b:
        result = gcd_calculation((a - b) / 2, b)
    return result


# create full sentence

def get_full_sentence(a, b, gcd_result):
    s = []
    s.append('{} {}'.format(str(a), str(b)))
    s.append(str(gcd_result))
    return s


# define function main

def main():
    item_count = 0
    s = []
    while item_count < _NUM_OF_CORR_ANSWERS:
        a = get_random_int(_RANDOM_RANGE)
        b = get_random_int(_RANDOM_RANGE)
        gcd = gcd_calculation(a, b)
        s.append(get_full_sentence(a, b, gcd))
        item_count += 1
    cli(s, _RULE)
    return None


# detect use type

if __name__ == '__main__':
    main()
