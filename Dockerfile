FROM python:3.12-slim
LABEL maintainer="musiychuk09@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR weather/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
