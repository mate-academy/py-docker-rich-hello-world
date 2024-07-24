FROM python:3.12-alpine
LABEL maintainer="comercaleuros@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app /app

CMD ["python", "main.py"]
