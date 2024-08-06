FROM python:3.12.4-alpine3.20
LABEL maintainer="stasiksudakov@gmail.com"

ENV PYTHONBUFFERED 1
WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]