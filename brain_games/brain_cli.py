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

_ROUNDS_COUNT = 3  # required number of correct answers

# input user


def get_user_input(greeting):
    return prompt.string(greeting)


# get game data for current round


def get_round_data(pointer_get_game_data):
    round_data_question, round_data_answer = pointer_get_game_data.main()
    return (round_data_question, round_data_answer)


def get_game_rule(pointer_get_game_data):
    round_data_rule = pointer_get_game_data._RULE
    return round_data_rule

# cli function. input data ->  [['1+2','3'], ['2-1','1'], ['10:2','5']]'


def execute_game(pointer_get_game_data):
    round_data_rule = \
        get_game_rule(pointer_get_game_data)
    print(_WEL_TO_BG)
    user_name = get_user_input(_REQ_NAME)  # enter username
    print(_HELLO.format(user_name))
    print(round_data_rule)
    for _ in range(_ROUNDS_COUNT):
        round_data_question, round_data_answer = \
            get_round_data(pointer_get_game_data)
        print(_QUESTION.format(round_data_question))
        user_response = get_user_input(_ANSWER)  # enter answer
        if user_response == round_data_answer:
            # correct response
            print(_ANSWER_TRUE)
        else:
            # end game, incorrect response
            print(_ANSWER_FAIL.format(user_response, round_data_answer))
            print(_OFFER.format(user_name))
            return
    # You are win!
    print(_CONGRATULATION.format(user_name))
    return
