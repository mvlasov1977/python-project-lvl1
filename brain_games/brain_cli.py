#!/usr/bin/env python3

import prompt

_WEL_TO_BG = 'Welcome to the Brain Games!'
_REQ_NAME = 'May I have your name? '
_HELLO = 'Hello, {}!'
_QUESTION = 'Question: {}'
_ANSWER = 'Your answer: '
_ANSWER_FAIL = "'{}' is wrong answer ;(. Correct answer was '{}'."
_OFFER = "Let's try again, {}!"
_ANSWER_TRUE = 'Correct!'
_CONGRATULATION = 'Congratulations, {}!'


# input user


def input_str(greeting):
    return prompt.string(greeting)


# cli function


def cli(comparison_data, rules):  # [['1+2','3'], ['2-1','1'], ['10:2','5']]'
    print(_WEL_TO_BG)
    user_name = input_str(_REQ_NAME)
    print(_HELLO.format(user_name))
    print(rules)
    correct_answers_cnt = 0
    while correct_answers_cnt < len(comparison_data):
        data_item = comparison_data[correct_answers_cnt]
        print(_QUESTION.format(data_item[0]))
        user_response = input_str(_ANSWER)
        if user_response == data_item[1]:
            # correct response
            correct_answers_cnt += 1
            print(_ANSWER_TRUE)
        else:
            # end game, incorrect response
            print(_ANSWER_FAIL.format(user_response, data_item[1]))
            print(_OFFER.format(user_name))
            return False
    if correct_answers_cnt == len(comparison_data):
        # You are win!
        print(_CONGRATULATION.format(user_name))
        return True
