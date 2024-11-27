FROM python:3.9-slim
LABEL maintainer="v.s.viesich@gmail.com"

ENV PYTHOUNNBUFFERED=1

WORKDIR /app/

COPY app/main.py /app/main.py

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "/app/main.py"]
