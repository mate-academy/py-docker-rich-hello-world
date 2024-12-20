FROM python:3.10.8-slim

WORKDIR /app

COPY app/main.py .

RUN pip install requests

CMD ["python", "main.py"]
