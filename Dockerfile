FROM python:3.11.6-alpine3.18
LABEL maintainer="clash2clans1one@gmail.com"

ENV PYTHOUNNBUFFERED 1
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]