# Makefile for  Vlasov Maksim project. Hexlet student 2021.

install:
	poetry install

brain-games:
	poetry run brain-games

test:
	echo "Test OK!"


# This names will ignore Make process
.PHONY: install brain-games test
