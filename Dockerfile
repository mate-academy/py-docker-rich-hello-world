FROM python:3.11-alpine3.18
LABEL maintainer="kbuchinskiywork@gmail.com"


ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
