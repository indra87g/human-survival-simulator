setup:
	@pip install -r requirements.txt

format:
	@black **/**/*.py

lint:
	@flake8 . > flake8-report.txt