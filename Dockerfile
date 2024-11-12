FROM python:3.12.3-alpine3.19
LABEL maintiner="oleksandrtaranenko239@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]
