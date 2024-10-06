FROM python:3.12.5-alpine3.20
LABEL maintainer="Sergio0bbb"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]