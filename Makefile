all: flake8 test
.PHONY: all

flake8:
	flake8 fastapi_sqlalchemy_example tests
.PHONY: flake8

test:
	pytest -xv tests
.PHONY: test

requirements.txt:
	virtualenv -p python3 venv
	venv/bin/pip3 install git+https://github.com/zuarbase/fastapi-sqlalchemy#egg=fastapi-sqlalchemy[dev,prod]
	venv/bin/pip3 install -e .[dev,prod]
	venv/bin/pip3 freeze | egrep -v "fastapi_sqlalchemy_example|pkg-resources" > $@
