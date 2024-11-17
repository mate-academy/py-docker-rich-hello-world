FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir requests

CMD ["python", "app/main.py"]
