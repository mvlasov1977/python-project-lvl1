# file games.py
# It is library for Brain Games project.
# Here are located repeatable function.
# Good luck.

from random import randint


# generate a random number


def get_random_number(range):
    begin, end = range
    return randint(begin, end)


# parity check


def get_parity(number):
    if number % 2 == 0:
        return True
    else:
        return False
