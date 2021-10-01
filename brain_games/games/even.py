from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


# initial parameters section


_RANDOM_RANGE = (1, 10)  # randomise range for randint function


# parity check


def is_even(number):
    return number % 2 == 0


# create full sentence for question


def create_condition_and_correct_answer(number_a):
    game_question = str(number_a)
    if is_even(number_a):
        game_answer = 'yes'
    else:
        game_answer = 'no'
    return game_question, game_answer


# define function main brain-even


def create_round_data():
    number_a = randint(*_RANDOM_RANGE)
    return create_condition_and_correct_answer(number_a)


# detect use type


if __name__ == '__main__':
    create_round_data()
