FROM python:3.11-slim
LABEL maintainer="posseydon87@gmail.com"

ENV PYTHONBUFERRED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["docker", "pull", "struhanets/docker-weather-api:latest"]