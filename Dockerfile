FROM python:3.12.5-alpine3.19
LABEL mainteirner="iramladanovych@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR ./

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "/app/main.py"]
