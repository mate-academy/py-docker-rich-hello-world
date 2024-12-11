FROM python:3.12.8-alpine
LABEL maintainer="sberdianskyi@mate.com"
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
