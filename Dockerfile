FROM python:3.10.14-alpine3.20
LABEL maintainer="dimon@gmail.com"

ENV PYTHOUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
