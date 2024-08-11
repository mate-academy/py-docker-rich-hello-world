FROM python:3.12-alpine3.19

LABEL authors="Boris"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]