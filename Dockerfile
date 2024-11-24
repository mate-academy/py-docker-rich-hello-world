FROM python:3.14.0a2-alpine3.20
LABEL maintainer="alex.panzhar1@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
COPY app/main.py /app/main.py

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
