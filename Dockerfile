FROM python:alpine3.19
LABEL maintainer="max@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
