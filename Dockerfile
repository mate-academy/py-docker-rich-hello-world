FROM python:3.10.8-slim
LABEL mainteirner="hbaklanova@gmail.com"


ENV PYTHONNBUFFERD 1

WORKDIR /home/halyna/projects/py-docker-weather-api/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
