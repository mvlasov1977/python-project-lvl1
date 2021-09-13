#!/usr/bin/env python3

from brain_games.games_support import get_random_number, is_even

_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


# initial parameters section


_RANDOM_RANGE = (1, 10)  # randomise range for randint function


# create full sentence for question


def get_full_sentence(number_a):
    sentence_list = []
    sentence_list.append(number_a)
    if is_even(number_a):
        sentence_list.append('yes')
    else:
        sentence_list.append('no')
    return sentence_list


# define function main brain-even


def main():
    number_a = get_random_number(_RANDOM_RANGE)
    return (get_full_sentence(number_a), _RULE)


# detect use type


if __name__ == '__main__':
    main()
