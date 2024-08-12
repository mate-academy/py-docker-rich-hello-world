FROM python:3.10.8-slim

LABEL authors="Boris"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
