#!/usr/bin/env python3

import prompt
from random import randint

_WEL_TO_BG = 'Welcome to the Brain Games!'
_REQ_NAME = 'May I have your name? '
_HELLO = 'Hello, {}!'
_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
_QUESTION = 'Question: {}'
_ANSWER = 'Your answer: '
_ANSWER_FAIL = "'{}' is wrong answer ;(. Correct answer was '{}'."
_OFFER = "Let's try again, {}!"
_ANSWER_TRUE = 'Correct!'
_CONGRATULATION = 'Congratulation, {}!'


# initial parameters section


_RANDOM_RANGE = (1, 100)  # randomise range for randint function
_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers


# parity check


def parity_chk(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


# input user


def input_str(greeting):
    return prompt.string(greeting)


# generate a random number


def get_random_int(range):
    begin, end = range
    return randint(begin, end)


# define function main


def main():
    print(_WEL_TO_BG)
    user_name = input_str(_REQ_NAME)
    print(_HELLO.format(user_name))
    print(_RULE)
    correct_answers_cnt = 0
    while correct_answers_cnt < _NUM_OF_CORR_ANSWERS:
        random_number = get_random_int(_RANDOM_RANGE)
        print(_QUESTION.format(random_number))
        user_response = input_str(_ANSWER)
        if user_response == parity_chk(random_number):
            # correct response
            correct_answers_cnt += 1
            print(_ANSWER_TRUE)
        else:
            # end game, incorrect response
            print(_ANSWER_FAIL.format(user_response, parity_chk(random_number)))
            print(_OFFER.format(user_name))
            break
    if correct_answers_cnt == _NUM_OF_CORR_ANSWERS:
        # You are win!
        print(_CONGRATULATION.format(user_name))


# detect use type


if __name__ == '__main__':
    main()
