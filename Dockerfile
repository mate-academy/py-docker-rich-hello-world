# Use a minimal Python image
FROM python:3.9-slim

# Metadata
LABEL maintainer="szholudsd@gmail.com"

# Set environment variables to prevent Python from buffering outputs
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
COPY app/ ./app/

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "app/main.py"]
