FROM python:3.13.0b1-alpine3.20

LABEL authors="dmytro.hlazyrin@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
