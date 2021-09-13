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

_NUM_OF_CORR_ANSWERS = 3  # required number of correct answers

# input user


def get_user_input(greeting):
    return prompt.string(greeting)


# get game data for current round


def get_comparison_data(pointer_get_game_data):
    comparison_data, rules = pointer_get_game_data()
    return (comparison_data, rules)


# cli function


def cli(pointer_get_game_data):  # [['1+2','3'], ['2-1','1'], ['10:2','5']]'
    comparison_data, rules = get_comparison_data(pointer_get_game_data)
    print(_WEL_TO_BG)
    user_name = get_user_input(_REQ_NAME)  # enter username
    print(_HELLO.format(user_name))
    print(rules)
    correct_answer_cnt = 0
    while correct_answer_cnt < _NUM_OF_CORR_ANSWERS:
        comparison_data, rules = get_comparison_data(pointer_get_game_data)
        data_item = comparison_data
        print(_QUESTION.format(data_item[0]))
        user_response = get_user_input(_ANSWER)  # enter answer
        if user_response == data_item[1]:
            # correct response
            correct_answer_cnt += 1
            print(_ANSWER_TRUE)
        else:
            # end game, incorrect response
            print(_ANSWER_FAIL.format(user_response, data_item[1]))
            print(_OFFER.format(user_name))
            return False
    if correct_answer_cnt == len(comparison_data):
        # You are win!
        print(_CONGRATULATION.format(user_name))
        return True
