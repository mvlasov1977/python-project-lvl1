#!/usr/bin/env python3

from random import choice, randint

GAME_RULE = 'What is the result of the expression?'


# initial parameters section


_RANDOM_RANGE = (1, 10)  # randomise range for randint function
_OPERATION = ['+', '-', '*']


# create full sentence for question


def create_condition_and_correct_answer(number_a, number_b, operation):
    game_question = str(number_a) + ' ' + operation + ' ' + str(number_b)
    if operation == '+':
        game_answer = number_a + number_b
    elif operation == '-':
        game_answer = number_a - number_b
    elif operation == '*':
        game_answer = number_a * number_b
    return (game_question, str(game_answer))


# define function main brain-calc


def create_round_data():
    oprnd_a = randint(*_RANDOM_RANGE)
    oprnd_b = randint(*_RANDOM_RANGE)
    calc_operation = choice(_OPERATION)
    return create_condition_and_correct_answer(oprnd_a,
                                               oprnd_b,
                                               calc_operation)


# detect use type


if __name__ == '__main__':
    create_round_data()
