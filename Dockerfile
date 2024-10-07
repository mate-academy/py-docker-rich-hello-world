FROM python:3.12.5
LABEL maintainer="vlada.belayy@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app/main.py"]