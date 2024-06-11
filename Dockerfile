FROM python:3.10
LABEL maintainer="vitalikbashkiser@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV API_KEY=""

CMD ["python", "app/main.py"]
