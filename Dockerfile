FROM python:3.11.8-alpine3.18
LABEL maintainer="ivchenkomykhailo@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "0.0.0.0:8000"]
