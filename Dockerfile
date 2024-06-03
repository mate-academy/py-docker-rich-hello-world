FROM python:3.9-slim
LABEL  maintainer="vitalinamalinovskaya557@gmail.com"

WORKDIR app/
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]