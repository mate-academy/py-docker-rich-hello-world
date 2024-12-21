ARG PYTHON_VERSION=3.10.8
FROM python:${PYTHON_VERSION}-slim as base
LABEL maintainer="yaroslavbordovoy@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . /app

CMD ["python", "app/main.py"]
