FROM python:3.11-slim

LABEL authors="mordegear90@gmail.com"

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests python-dotenv

CMD ["python", "app/main.py"]
