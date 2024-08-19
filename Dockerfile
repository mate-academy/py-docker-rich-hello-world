FROM python:3.10-slim
LABEL maintainer="developer14062007@gmail.com"


WORKDIR app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]