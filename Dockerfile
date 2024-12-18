FROM python:3.13.0-slim
LABEL authors="serhiik"

ENV PYTHONUNNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app/main.py"]