FROM python:3.9.20-alpine3.20
LABEL maintainer="serhido"

ENV PYTHONNBUFFERED=1

WORKDIR /app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/main.py .

CMD ["python", "/app/main.py"]
