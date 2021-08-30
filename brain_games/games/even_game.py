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


# create full sentence for question


def get_full_sentence(number_a):
    sentence_list = []
    sentence_list.append(number_a)
    sentence_list.append(parity_chk(number_a))
    return sentence_list


# define function main brain-even


def main():
    even_question_list = []
    item_count = 0
    while item_count < _NUM_OF_CORR_ANSWERS:
        number_a = get_random_int(_RANDOM_RANGE)
        even_question_list.append(get_full_sentence(number_a))
        item_count += 1
    cli(even_question_list, _RULE)
    return None


# detect use type


if __name__ == '__main__':
    main()
