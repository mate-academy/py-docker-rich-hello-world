FROM python:3.11.4-alpine
LABEL maintainer="volodymyr_dolgyi@ukr.net"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
