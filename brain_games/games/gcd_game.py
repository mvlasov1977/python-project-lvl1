#!/usr/bin/env python3

from brain_games.games_support import get_random_number, is_even

_RULE = 'Find the greatest common divisor of given numbers.'


# initial parameters section

_RANDOM_RANGE = (1, 10)  # randomise range for randint function


# gcd calculation (binary Evklid algorythm)

def gcd_calculation(a, b):
    if a == 0 and b != 0:
        result = b
    elif a != 0 and b == 0:
        result = a
    elif a == b:
        result = a
    elif a == 1 or b == 1:
        result = 1
    else:
        result = gcd_calculation_part2(a, b)
    return result


def gcd_calculation_part2(a, b):
    if is_even(a) and is_even(b):
        result = 2 * gcd_calculation(a // 2, b // 2)
    elif is_even(a) and not is_even(b):
        result = gcd_calculation(a // 2, b)
    elif not is_even(a) and is_even(b):
        result = gcd_calculation(a, b // 2)
    elif a < b:
        result = gcd_calculation((b - a) // 2, a)
    elif a > b:
        result = gcd_calculation((a - b) // 2, b)
    return result


# create full sentence for question

def get_full_sentence(number_a, number_b, gcd_result):
    sentence_list = []
    sentence_list.append('{} {}'.format(str(number_a), str(number_b)))
    sentence_list.append(str(gcd_result))
    return sentence_list


# define function main brain-gcd

def main():
    number_a = get_random_number(_RANDOM_RANGE)
    number_b = get_random_number(_RANDOM_RANGE)
    gcd = gcd_calculation(number_a, number_b)
    return (get_full_sentence(number_a, number_b, gcd), _RULE)


# detect use type

if __name__ == '__main__':
    main()
