install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv password_security.py

format:
	black *.py

lint:
	pylint --disable=R,C password_security.py

all: install lint test