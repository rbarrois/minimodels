PACKAGE=minimodel

all: default



default:


clean:
	find . -name '*.pyc' -delete
	find . -type d -empty -delete


test:
	python setup.py test

.PHONY: all default update
