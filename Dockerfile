FROM python:3.12-slim

LABEL maintainer="38cerg12021979@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/

CMD ["python", "main.py"]