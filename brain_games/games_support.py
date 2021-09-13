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


def is_even(number):
    return number % 2 == 0
