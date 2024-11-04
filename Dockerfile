FROM python:3.10.8-slim
LABEL authors="anton.verbovyi@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR app2/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir  -r requirements.txt

COPY . .

CMD ["python3", "app/main.py"]
