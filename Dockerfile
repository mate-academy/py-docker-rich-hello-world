FROM python:3.12-slim
LABEL authors="kates1999"

WORKDIR /py-docker-weather-api
COPY . .

RUN pip install requests

ENV PYTHONUNBUFFERED=1

CMD ["python", "app/main.py"]