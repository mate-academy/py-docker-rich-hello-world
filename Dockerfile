FROM python:3.12-slim

LABEL maintainer="aleksei.taran@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]