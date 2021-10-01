#!/usr/bin/env python3

from prompt import string

_ROUNDS_COUNT = 3  # required number of correct answers


# cli function. input data ->  [['1+2','3'], ['2-1','1'], ['10:2','5']]'


def execute(game_module):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')  # enter username
    print('Hello, {}!'.format(user_name))
    print(game_module.RULE)
    for _ in range(_ROUNDS_COUNT):
        question, correct_answer = \
            game_module.create_round_data()
        print('Question: {}'.format(question))
        user_response = string('Your answer: ')  # enter answer
        if user_response == correct_answer:
            # correct response
            print('Correct!')
        else:
            # end game, incorrect response
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(user_response, correct_answer))
            print("Let's try again, {}!".format(user_name))
            return
    # You are win!
    print('Congratulations, {}!'.format(user_name))
    return
