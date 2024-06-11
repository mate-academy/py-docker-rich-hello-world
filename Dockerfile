FROM python:3.12.3-alpine3.20

WORKDIR /app

COPY app .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]