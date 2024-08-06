FROM python:3.9-alpine3.18
LABEL maintainer="bogdn.zinchenko.2019@gmail.com"

ENV PYTHOUNNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app /app

CMD ["python", "main.py"]
