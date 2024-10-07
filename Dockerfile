FROM python:3.11-slim

LABEL maintainer="igorutkin2002@gmail.com"

ENV API_KEY="b7753729f72d44f8abc154909240710"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
