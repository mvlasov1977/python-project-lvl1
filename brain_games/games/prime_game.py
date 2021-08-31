#!/usr/bin/env python3

from brain_games.games_support import get_random_int
from brain_games.brain_cli import cli

_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# initial parameters section

_RANDOM_RANGE = (1, 100)  # rand fst number for randint function
_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers


# calculate main number

def main_number(a):
    if a > 1:
        subsequence = range(2, a - 1)
        for x in subsequence:
            if a % x == 0:
                return 'no'
        else:
            return 'yes'
    return 'no'


# create full sentence for question

def get_full_sentence(random_number):
    sentence_list = []
    sentence_list.append(str(random_number))
    sentence_list.append(main_number(random_number))
    return sentence_list


# define function main brain-prime

def main():
    item_count = 0
    prime_question_list = []
    while item_count < _NUM_OF_CORR_ANSWERS:
        a = get_random_int(_RANDOM_RANGE)
        prime_question_list.append(get_full_sentence(a))
        item_count += 1
    cli(prime_question_list, _RULE)
    return None


# detect use type

if __name__ == '__main__':
    main()
