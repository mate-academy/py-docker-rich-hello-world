FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/

RUN pip install requests

CMD ["python", "main.py"]
