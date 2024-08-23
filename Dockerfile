FROM python:3.11.6-alpine
LABEL maintainer="playfog3@gmail.com"

ENV PYTHONNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
