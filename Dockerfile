FROM python:3.10.12-alpine3.17

LABEL maintainer='mykm3ua@gmail.com'

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "app/main.py"]