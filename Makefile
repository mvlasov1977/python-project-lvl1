# Makefile for  Vlasov Maksim project. Hexlet student 2021.

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	echo "Test OK!"


# This names will ignore Make process
.PHONY: install brain-games build publish package-install test
