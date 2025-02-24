install:
	uv pip install -r requirements/requirements.txt

run:
	#fastapi dev app/main.py
	python -m uvicorn app.main:app --reload
