FROM python:3.11.6-alpine3.18
LABEL maintailer="igor2tak2212@gmail.com"

ENV PYTHOUNNBUFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
