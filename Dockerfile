FROM python:3.11.6-slim
LABEL maintainer="oleksiukstepann@gmail.com"

ENV PYTHOUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
