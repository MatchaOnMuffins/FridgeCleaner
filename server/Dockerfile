# Use the official Python image as a base
FROM python:3.11-slim

# Set environment variables to avoid buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Default command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]