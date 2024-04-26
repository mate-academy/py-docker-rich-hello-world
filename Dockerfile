FROM python:3.12-alpine3.19
LABEL maintainer="makslapchuk@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app/main.py"]