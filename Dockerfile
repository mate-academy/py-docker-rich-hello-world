FROM python:3.12-slim
LABEL maintainer="andrii.khamaza0@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/

CMD ["python", "main.py"]