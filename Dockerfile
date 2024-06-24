FROM python:3.10.14-alpine3.20
LABEL maintainer="dmytroshchoma@gmail.com"

ENV PYTHOUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app/main.py"]
