FROM python:3.12-slim

WORKDIR /app

COPY app .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]