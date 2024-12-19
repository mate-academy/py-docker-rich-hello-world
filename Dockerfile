FROM python:3.11.11-slim
LABEL maintainer="leon.kushnir15@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "manage.py", "runserver", "0.0.0.0:8000"]

# For run docker:   docker run -p 8001:8000 --env-file .env killmont/docker-weather-api
