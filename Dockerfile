FROM python:3.11-alpine3.18
LABEL maintainer="nikset1@gmail.com"


ENV PYTHOUNNBUFFERED 1

WORKDIR weather_api/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . .

CMD ["python", "app/main.py"]