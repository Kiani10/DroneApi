# Use a base Python image
FROM python:3.11-slim

# Install system dependencies needed for pyodbc
RUN apt-get update && \
    apt-get install -y unixodbc-dev libodbc1 libodbc2 libodbcinstq4-dev gcc g++ && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
