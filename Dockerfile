FROM python:3.10.5-slim
LABEL maintainer="nykytakuzmytskyi@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
