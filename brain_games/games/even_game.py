#!/usr/bin/env python3

from brain_games.games_support import get_random_number

_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


# initial parameters section


_RANDOM_RANGE = (1, 10)  # randomise range for randint function


# parity check


def is_even(number):
    return number % 2 == 0


# create full sentence for question


def create_game_data(number_a):
    game_question = str(number_a)
    if is_even(number_a):
        game_answer = 'yes'
    else:
        game_answer = 'no'
    return game_question, game_answer


# define function main brain-even


def main():
    number_a = get_random_number(_RANDOM_RANGE)
    return create_game_data(number_a)


# detect use type


if __name__ == '__main__':
    main()
