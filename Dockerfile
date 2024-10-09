FROM python:3.9-slim

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app /app

CMD ["python", "main.py"]
