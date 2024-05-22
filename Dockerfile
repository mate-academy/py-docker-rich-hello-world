FROM python:3.12-alpine
LABEL maintainer="vitaliyburkalo81@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
