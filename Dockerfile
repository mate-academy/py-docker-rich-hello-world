FROM python:3.12-slim
LABEL maintainer="d.villarionovich@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app .

ENTRYPOINT ["python", "main.py"]
