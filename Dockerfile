FROM python:3.11.6-alpine3.18
LABEL maintainer="dkotkod@gmail.com"

WORKDIR app/
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
