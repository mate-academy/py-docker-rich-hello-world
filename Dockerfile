FROM python:3.11-slim
LABEL maintainer="sanyok.it@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/


EXPOSE 8000

CMD ["python", "main.py"]
