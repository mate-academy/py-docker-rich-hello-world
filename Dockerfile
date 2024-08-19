FROM python:3.10
LABEL maintainer="developer14062007@gmail.com"

ENV PYTHONUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]