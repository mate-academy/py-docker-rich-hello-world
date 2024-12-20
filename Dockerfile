ARG PYTHON_VERSION=3.10.8
FROM python:${PYTHON_VERSION}-slim as base
LABEL maintainer="yaroslavbordovoy@gmail.com"


ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app/main.py"]
