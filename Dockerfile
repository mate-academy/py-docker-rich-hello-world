FROM alpine3.18
LABEL maintainer = 'kritvladislav98@gmail.com'

ENV PYTHONBUFFERED 1

WORKDIR /app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py"]
