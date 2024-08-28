FROM python:3.11-alpine
LABEL maintainer="olena.kalitsinka@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/weather/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "0.0.0.0.8000"]
