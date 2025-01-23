FROM python:3.12-alpine3.21
LABEL authors="Dell"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
