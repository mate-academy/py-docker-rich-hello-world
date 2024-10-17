FROM python:3.12-alpine
LABEL maintainer="bladeryz@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
