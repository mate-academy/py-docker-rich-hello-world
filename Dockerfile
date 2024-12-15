FROM python:3.11.6-alpine3.18

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D myuser
USER myuser

COPY . .

CMD ["python3", "app/main.py"]