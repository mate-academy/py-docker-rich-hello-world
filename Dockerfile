FROM python:3.11.6-alpine3.18
LABEL maintainer="savenya2013@gmail.com"

ENV PYTHONDONTWRITECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 8000

CMD ["python", "app/main.py"]
