FROM python:3.9.20-alpine3.20
LABEL maintainer="olenacherneha@proton.me"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env

COPY . .

CMD ["python", "app/main.py"]
