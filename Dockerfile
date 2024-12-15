FROM python:3.12-alpine3.21
LABEL maintainer="dmysamo@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR forecast_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
