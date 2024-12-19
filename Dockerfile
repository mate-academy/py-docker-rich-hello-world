FROM python:3.11-slim
LABEL maintainer="silva.vvss12@gmail.com"

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]