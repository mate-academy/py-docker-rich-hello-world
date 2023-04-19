FROM python:3.10.4-slim
LABEL maintainer="=misternictof@gmail.com"

ENV PYTHONUNBEFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
