FROM python:3.12-alpine
LABEL maintainer="1.2.aznch@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
