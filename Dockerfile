FROM python:3.11-slim
LABEL maintainer="ffspitfire808@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/main.py

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
