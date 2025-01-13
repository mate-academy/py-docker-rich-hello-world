FROM python:3.9-slim
LABEL maintainer="vladrymarchuk@gmai.com"


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/main.py /app

CMD ["python", "main.py"]
