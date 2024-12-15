FROM python:3.12-slim
LABEL maintainer="mxbely98@gmail.com"

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
