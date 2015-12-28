.PHONY: help clean clean-pyc clean-build lint test test-all coverage sdist

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-test - remove test artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "sdist - package"

clean: clean-build clean-test clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-test:
	rm -fr .cache/
	rm -fr .eggs/
	rm -fr .tox/
	rm -f .coverage
	rm -f test.db

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 djangoseo tests

test:
	python setup.py test

coverage:
	coverage run --rcfile=.coveragerc setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

sdist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
