FROM python:3.12.3-slim
LABEL maintainer="94nj111@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=True
ENV PYTHONUNBUFFERED=True

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN pip install --no-cache-dir requests

USER appuser

COPY app/main.py /app/main.py

EXPOSE 8000

CMD ["python", "main.py"]
