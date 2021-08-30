#!/usr/bin/env python3

from random import randint
from brain_games.brain_cli import cli

_RULE = 'What number is missing in the progression?'


# initial parameters section

_RANDOM_RANGE_FIRST_NUMBER = (1, 30)  # rand fst number for randint function
_RANDOM_RANGE_INCREMENT_NUMBER = (1, 10)  # rand increment for randint function
_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers
_LENGTH_OF_PROGRESSION = 10  # length of arithmetic progression
_RANDOM_RANGE_SECRET_NUMBER = (1, _LENGTH_OF_PROGRESSION)  # rand sec num range
_SECRET_MASK = '..'  # secret mask indicate secret number progression


# generate a random number

def get_random_int(range):
    begin, end = range
    return randint(begin, end)


# create full sentence for question

def get_full_sentence(first_number, step, secret_number, p_length):
    sentence_list = []
    progression = ''
    index = 0
    while index < p_length:
        element = first_number + index * step
        if index != 0:
            progression = progression + ' '
        if index == secret_number - 1:
            progression = progression + _SECRET_MASK
            secret_element = element
        else:
            progression = progression + str(element)
        index += 1
    sentence_list.append(progression)
    sentence_list.append(str(secret_element))
    return sentence_list


# define function main brain-progression

def main():
    item_count = 0
    s = []
    while item_count < _NUM_OF_CORR_ANSWERS:
        first_number = get_random_int(_RANDOM_RANGE_FIRST_NUMBER)
        step = get_random_int(_RANDOM_RANGE_INCREMENT_NUMBER)
        secret_number = get_random_int(_RANDOM_RANGE_SECRET_NUMBER)
        len_prg = _LENGTH_OF_PROGRESSION
        s.append(get_full_sentence(first_number, step, secret_number, len_prg))
        item_count += 1
    cli(s, _RULE)
    return None


# detect use type

if __name__ == '__main__':
    main()
