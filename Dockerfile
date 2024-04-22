FROM python:3.12
LABEL maintainer="2ilgan1601@gmail.com"
ENV PYTHONUNBUFFERED 1
WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app/ /app
ENV API_KEY=0
CMD ["python", "main.py"]
