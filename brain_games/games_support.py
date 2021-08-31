# file games.py
# It is library for Brain Games project.
# Here are located repeatable function.
# Good luck.

from random import randint


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
