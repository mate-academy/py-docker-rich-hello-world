FROM python:3.11-alpine3.18

#  author of image
LABEL maintainer="alona.sorochynska@gmail.com"

#  python shouldn't buffer its messages
ENV PYTHOUNNBUFFERED 1

WORKDIR app/

#  source -> container
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#  copy from current dir (root) to current dir (app/)
COPY . .

# run command
CMD ["python", "app/main.py"]
