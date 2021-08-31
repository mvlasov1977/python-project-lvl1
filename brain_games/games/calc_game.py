#!/usr/bin/env python3

from random import choice
from brain_games.games_support import get_random_number
from brain_games.brain_cli import cli

_RULE = 'What is the result of the expression?'


# initial parameters section


_RANDOM_RANGE = (1, 10)  # randomise range for randint function
_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers
_OPERATION = ['+', '-', '*']


# generate a random operation


def get_random_operation(range):
    return choice(range)


# create full sentence for question


def get_full_sentence(number_a, number_b, operation):
    sentence_list = []
    sentence_list.append(str(number_a) + ' ' + operation + ' ' + str(number_b))
    if operation == '+':
        sentence_list.append(str(number_a + number_b))
        return sentence_list
    elif operation == '-':
        sentence_list.append(str(number_a - number_b))
        return sentence_list
    elif operation == '*':
        sentence_list.append(str(number_a * number_b))
        return sentence_list
    else:
        return None  # generate exception


# define function main brain-calc


def main():
    item_count = 0
    calc_q_lst = []
    while item_count < _NUM_OF_CORR_ANSWERS:
        oprnd_a = get_random_number(_RANDOM_RANGE)
        oprnd_b = get_random_number(_RANDOM_RANGE)
        calc_operation = get_random_operation(_OPERATION)
        calc_q_lst.append(get_full_sentence(oprnd_a, oprnd_b, calc_operation))
        item_count += 1
    cli(calc_q_lst, _RULE)
    return None


# detect use type


if __name__ == '__main__':
    main()
