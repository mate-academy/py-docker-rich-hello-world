FROM python:3.9-slim
LABEL maintaner="dimasysoev20000@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]