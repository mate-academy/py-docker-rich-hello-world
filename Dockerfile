FROM python:3.10.8-slim
LABEL maintainer="waliker448gmail.com"
ENV PYTHOUNNBUFFERED 1
WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
