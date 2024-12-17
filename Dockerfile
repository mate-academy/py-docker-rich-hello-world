ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim as base
LABEL maintainer="dmysamo@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

WORKDIR /app

COPY . /app

RUN chown -R appuser:appuser /app

USER appuser

RUN pip install --no-cache-dir --user -r requirements.txt

EXPOSE 8000

CMD ["python", "app/main.py"]
