FROM python:3.11-alpine
LABEL maintainer="maksss196@gamil.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/main.py

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
