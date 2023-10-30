FROM python:3.11.4-slim
LABEL maintainer="e.nagolyuk@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


CMD ["python", "app/main.py"]
