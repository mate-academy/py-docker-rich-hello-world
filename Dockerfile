FROM python:3.11
LABEL maintainer="arsen.test.mess@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
