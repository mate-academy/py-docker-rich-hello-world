FROM python:3.12-alpine3.18
LABEL maintainer="roman"

ENV PYTHOUNNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]