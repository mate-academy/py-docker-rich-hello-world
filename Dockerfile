FROM python:3.11-slim
LABEL authors="specializedDev"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV API_KEY=${API_KEY}

CMD ["python", "app/main.py"]
