FROM python:3.11
LABEL maintainer="maksym.protsak@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pin install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
