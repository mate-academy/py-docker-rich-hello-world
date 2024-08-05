FROM python:3.12.0rc2-alpine3.18
LABEL mainteirner="info47580@gmail.com"

ENV PYTHONNBUFFERD 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
