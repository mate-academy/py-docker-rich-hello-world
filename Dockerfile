FROM python:3.12.2-slim

LABEL authors="rusipbox@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

CMD ["python", "main.py"]
