.PHONY: help install dev api dashboard test clean

help:
@echo "Available commands:"
@echo " install Install dependencies"
@echo " api Start API server"
@echo " dashboard Start dashboard"
@echo " test Run tests"
@echo " clean Clean cache"

install:
pip install -r requirements.txt

api:
python -m api.server --reload

dashboard:
streamlit run dashboard/app.py

test:
pytest tests/ -v

clean:
find . -type f -name "*.pyc" -delete
find . -type d -name "pycache" -delete
