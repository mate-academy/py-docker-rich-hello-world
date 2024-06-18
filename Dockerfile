FROM python:3.11.6-alpine3.18

LABEL maintainer="mr.darmstadtium@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY app .
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

<<<<<<< HEAD
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user

#CMD ["python", "manage", "runserver", "0.0.0.0:8000"] - delete this line
=======
CMD ["python", "main.py"]
>>>>>>> b15c7dcec6f274b3bb6ee2264efbc4545a737864
