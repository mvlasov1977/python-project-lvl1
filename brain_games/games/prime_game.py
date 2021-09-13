#!/usr/bin/env python3

from brain_games.games_support import get_random_number

_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# initial parameters section

_RANDOM_RANGE = (1, 100)  # rand fst number for randint function


# calculate main number

def is_prime(a):
    if a > 1:
        subsequence = range(2, a - 1)
        for x in subsequence:
            if (a % x == 0):
                return False
        else:
            return True
    return False


# create full sentence for question

def get_full_sentence(random_number):
    sentence_list = []
    sentence_list.append(str(random_number))
    if is_prime(random_number):
        sentence_list.append('yes')
    else:
        sentence_list.append('no')
    return sentence_list


# define function main brain-prime

def main():
    a = get_random_number(_RANDOM_RANGE)
    return (get_full_sentence(a), _RULE)


# detect use type

if __name__ == '__main__':
    main()
