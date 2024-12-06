FROM python:3.12-slim
LABEL maintainer="arsen.markotskyi@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

# Встановлення залежностей
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]
