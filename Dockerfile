FROM python:3.12-alpine
LABEL maintainer="ohnooq1@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/
EXPOSE 8000

CMD ["python", "app/main.py"]