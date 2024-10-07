FROM python:3.12.7-alpine3.20
LABEL maintainer="dsahalatyi@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app/main.py"]
