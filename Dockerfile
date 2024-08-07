FROM python:3.9-slim
LABEL authors="ivan.seeker6@gmail.com"

ENV PYTHONUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/main.py /app/

CMD ["python", "main.py"]
