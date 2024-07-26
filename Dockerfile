FROM python:3.10.8-slim
LABEL maintailer="igor2tak2212@gmail.com"

ENV PYTHOUNNBUFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
