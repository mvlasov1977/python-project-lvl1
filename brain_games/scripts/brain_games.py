#!/usr/bin/env python3

from brain_games.cli import welcome_user

_WELCOME = 'Welcome to the Brain Games!'
_WELCOME1 = 'May I have your name? '
_RESPOND = 'Hello, {}!'

# print welcome message :)
def welcome_print(txt):
     print(txt)

# define function main
def main():
    welcome_print(_WELCOME)
    print(_RESPOND.format(welcome_user(_WELCOME1)))
# detect use type 
if __name__ == '__main__':
     main()
