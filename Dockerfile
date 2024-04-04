FROM python:3.11.0-slim
LABEL maintainer="mr.skyrda@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY

WORKDIR docker_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python -m dotenv -f .env python app/main.py"]
