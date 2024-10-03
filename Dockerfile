FROM python:3.12-alpine
LABEL author="iamlucky1990@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY project_requirements.txt project_requirements.txt

RUN pip install --no-cache-dir -r project_requirements.txt

COPY . .

CMD ["python", "app/main.py"]
