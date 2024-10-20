FROM python:3.9-alpine
LABEL maintainer="jyjuk1@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY app /app

CMD ["python", "main.py"]
