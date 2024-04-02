FROM python:3.12.0-alpine3.18
LABEL maintainer="interchanal@ukr.net"

ENV PYTHONBUFFERED 1

WORKDIR weather-api/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
