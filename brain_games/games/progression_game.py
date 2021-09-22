#!/usr/bin/env python3

from brain_games.games_support import get_random_number

_RULE = 'What number is missing in the progression?'


# initial parameters section

_RANDOM_RANGE_FIRST_MEMBER = (1, 30)  # rand fst number for randint function
_RANDOM_RANGE_COMMON_DIFFERENCE = (1, 10)  # rand increment for randint function
_NUMBER_OF_TERMS = 10  # length of arithmetic progression
_RANDOM_RANGE_SECRET_MEMBER_INDEX = (1, _NUMBER_OF_TERMS)  # rand sec num range
_SECRET_MASK = '..'  # secret mask indicate secret number progression
_PROGRESSION_SEPARATOR = ' '


# create arithmetic_progression


def get_finite_arithmetic_progression(first_member,
                                      common_difference,
                                      number_of_terms):
    arithmetic_series = []
    last_member = first_member + common_difference * (number_of_terms - 1)
    for member in range(first_member, last_member + 1, common_difference):
        arithmetic_series.append(member)
    return arithmetic_series


# convert arithmetic_progression to text


def stringify_arithmetic_progression(arithmetic_series):
    stringify_arithmetic_series = []
    for member in arithmetic_series:
        stringify_arithmetic_series.append(str(member))
    return stringify_arithmetic_series


# create full sentence for question


def create_game_data(first_member,
                     common_difference,
                     secret_member_index,
                     number_of_terms,
                     secret_mask):
    finite_arithmetic_progression = \
        get_finite_arithmetic_progression(first_member,
                                          common_difference,
                                          number_of_terms)
    arithmetic_series = \
        stringify_arithmetic_progression(finite_arithmetic_progression)
    secret_member = arithmetic_series[secret_member_index - 1]
    arithmetic_series[secret_member_index - 1] = secret_mask
    game_question = _PROGRESSION_SEPARATOR.join(arithmetic_series)
    game_answer = secret_member
    return game_question, game_answer


# define function main brain-progression


def main():
    first_member = get_random_number(_RANDOM_RANGE_FIRST_MEMBER)
    common_difference = get_random_number(_RANDOM_RANGE_COMMON_DIFFERENCE)
    secret_member_index = get_random_number(_RANDOM_RANGE_SECRET_MEMBER_INDEX)
    number_of_terms = _NUMBER_OF_TERMS
    return create_game_data(first_member,
                            common_difference,
                            secret_member_index,
                            number_of_terms, _SECRET_MASK)


# detect use type

if __name__ == '__main__':
    main()
