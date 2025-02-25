install:
	uv pip install -r requirements/requirements.txt

run:
	python -m uvicorn app.main:app --reload

test:
	pytest -v

lint:
	ruff check --fix
	ruff format app tests
