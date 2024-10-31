# Use the official Python image as a base
FROM python:3.10-slim

# Install system dependencies, including libodbc
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your project files to the container
COPY . /app

# Install Python dependencies
RUN pip install -r req.txt

# Expose the port your app runs on (optional if Railway sets it automatically)
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
