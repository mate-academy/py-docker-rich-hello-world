FROM python:3.12.3-alpine3.19
LABEL maintainer="oleksii.kiva@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR app/

COPY requirements_for_docker.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
