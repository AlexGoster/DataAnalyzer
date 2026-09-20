.PHONY: test lint format clean install

test:
	python -m pytest tests/ -v

lint:
	python -m py analyzer/ cli.py

format:
	python -m black analyzer/ tests/ cli.py

clean:
	rm -rf output/*.html output/*.png output/*.svg
	rm -rf __pycache__ analyzer/__pycache__ tests/__pycache__
	rm -rf *.egg-info dist build

install:
	pip install -r requirements.txt

run:
	python cli.py analyze data/sample.csv
