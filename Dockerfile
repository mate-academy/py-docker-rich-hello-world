FROM python:3.11-alpine
LABEL maintainer="marina.ua13@gmail.com"
ENV PYTHOUNNBUFFERED 1
WORKDIR app/main.py
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
CMD ["python", "main.py"]
