FROM python:3.10-alpine3.17
LABEL authors="Victor"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app/main.py"]
