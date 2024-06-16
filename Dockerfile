FROM python:3.12.2-alpine3.19
LABEL maintainer="dmytro@yefimenko.com"

ENV PYTHONBUFFERED 1

WORKDIR weather-api/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
