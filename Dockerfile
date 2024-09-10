FROM python:3.11.5-alpine3.18
LABEL me="mishelgrotskis@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
