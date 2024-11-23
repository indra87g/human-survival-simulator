setup:
	@python -m venv .venv

format:
	@black **/**/*.py

lint:
	@flake8 . > flake8-report.txt