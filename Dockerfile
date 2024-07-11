FROM python:3.11-alpine3.20
LABEL authors="specializedDev"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV API_KEY=${API_KEY}

CMD ["python", "app/main.py", "0.0.0.0:8000"]

# docker run -e API_KEY=$API_KEY your_docker_image
