FROM python:3.9-slim
LABEL maintainer="evgennia.kondrashova@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR app/

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]

EXPOSE 3000
