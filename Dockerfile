FROM python:3.9.19-slim-bullseye
LABEL authors="Fedot0v"

ENV PYTHONNBUFFERED=1

WORKDIR /app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .. .

CMD ["python", "app/main.py"]
