FROM python:3.10.4-alpine
LABEL maintainer="cheshko.sergey@example.com"

ENV PYTHONUNBUFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
