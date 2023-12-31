install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_app.py

format:
	black examples/*.py exercises/*.py

lint:
	pylint --disable=R,C *.py

all: install lint test format