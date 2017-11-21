develop: install-python
	@echo ""

develop-only: develop

install-python:
	# must be executed serialially
	$(MAKE) install-python-base

install-python-base:
	@echo "--> Installing Python dependencies"
	pip install "setuptools>=0.9.8" "pip>=8.0.0"
	# order matters here, base package must install first
	pip install -e .
	pip install "file://`pwd`#egg=clab[dev]"

build: develop freeze dist
	@echo ""

locale:
	cd src/clab && clab django makemessages -i static -l en
	cd src/clab && clab django compilemessages
	@echo ""

freeze:
	cd src/clab && clab django collectstatic --noinput
	@echo ""

clean:
	@echo "--> Cleaning static cache"
	rm -rf dist/*
	@echo "--> Cleaning pyc files"
	find . -name "*.pyc" -delete
	@echo "--> Cleaning python build artifacts"
	@echo ""

dist:
	python setup.py sdist

.PHONY: develop build dist
