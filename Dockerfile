FROM python:3.12-slim
LABEL maintainer="jacktyler2391@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /py-docker-weather-api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]