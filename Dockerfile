FROM python:3.12.1-slim
LABEL maintainer="ilaruslanovich7@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app .

CMD ["python", "main.py"]