FROM python:3.11.6-alpine3.18

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]