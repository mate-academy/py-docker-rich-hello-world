FROM python:3.12.3-alpine3.18
LABEL maintrainer="vidernykov.a.e@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR ./

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
