FROM python:3.12.4-alpine

LABEL maintainer="lobachyakiv@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
