#!/usr/bin/env python3

from brain_games.games_support import get_random_number

_RULE = 'Find the greatest common divisor of given numbers.'


# initial parameters section

_RANDOM_RANGE = (1, 10)  # randomise range for randint function


# gcd calculation (binary Evklid algorythm)

def get_gcd(number_a, number_b):
    if (number_a == number_b):
        return number_a
    elif (number_a == 1 or number_b == 1):
        return 1
    elif (number_a > number_b):
        modulo = number_a % number_b
        if modulo == 0:
            return number_b
        else:
            return get_gcd(modulo, number_b)
    else:
        modulo = number_b % number_a
        if modulo == 0:
            return number_a
        else:
            return get_gcd(modulo, number_a)
    return None


# create full sentence for question

def create_game_data(number_a, number_b, gcd_result):
    sentence_list = []
    sentence_list.append('{} {}'.format(str(number_a), str(number_b)))
    sentence_list.append(str(gcd_result))
    return sentence_list


# define function main brain-gcd

def main():
    number_a = get_random_number(_RANDOM_RANGE)
    number_b = get_random_number(_RANDOM_RANGE)
    gcd = get_gcd(number_a, number_b)
    return (create_game_data(number_a, number_b, gcd), _RULE)


# detect use type

if __name__ == '__main__':
    main()
