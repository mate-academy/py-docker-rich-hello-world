FROM python:3.12.5-alpine3.19
LABEL maintainer="maksimnimitch@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]
