#!/usr/bin/env python3

from brain_games.games_support import get_random_number

_RULE = 'Find the greatest common divisor of given numbers.'


# initial parameters section

_RANDOM_RANGE = (1, 10)  # randomise range for randint function


# gcd calculation (binary Evklid algorythm)

def get_gcd(number_a, number_b):
    number_a, number_b = max(number_a, number_b), min(number_a, number_b)
    modulo = number_a % number_b
    if modulo == 0:
        return number_b
    else:
        return get_gcd(modulo, number_b)


# create full sentence for question

def create_game_data(number_a, number_b, gcd_result):
    game_question = '{} {}'.format(str(number_a), str(number_b))
    game_answer = str(gcd_result)
    return game_question, game_answer


# define function main brain-gcd

def main():
    number_a = get_random_number(_RANDOM_RANGE)
    number_b = get_random_number(_RANDOM_RANGE)
    gcd = get_gcd(number_a, number_b)
    return create_game_data(number_a, number_b, gcd)


# detect use type

if __name__ == '__main__':
    main()
