FROM python:alpine3.19
LABEL maintainer="roman.hlodann@gmail.com"

WORKDIR weather_api/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
