# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/main.py /app/main.py
RUN pip install --no-cache requests

# Set the command to run the script
CMD ["python", "main.py"]
