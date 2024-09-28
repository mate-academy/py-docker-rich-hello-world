FROM python:3.9.20-alpine3.20
LABEL authors="tkachuk1"

ENV PYTHONNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .. .

CMD ["python", "app/main.py"]
