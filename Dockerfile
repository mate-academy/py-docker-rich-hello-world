FROM python:3.12.3-slim
LABEL maintainer="94nj111@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/main.py /app/main.py

RUN pip install --no-cache-dir requests

CMD ["python", "main.py"]
