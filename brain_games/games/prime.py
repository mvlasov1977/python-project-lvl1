from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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

def create_condition_and_correct_answer(random_number):
    game_question = str(random_number)
    if is_prime(random_number):
        game_answer = 'yes'
    else:
        game_answer = 'no'
    return game_question, game_answer


# define function main brain-prime

def create_round_data():
    a = randint(*_RANDOM_RANGE)
    return create_condition_and_correct_answer(a)


# detect use type

if __name__ == '__main__':
    create_round_data()
