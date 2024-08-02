FROM python:3.10.14-alpine3.20
LABEL maintainer="tiunovmixs@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR weather/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
