# Use a specific version of Python as the base image
FROM python:3.11

# Install system dependencies needed for pyodbc and ODBC Driver 17 for SQL Server
RUN apt-get update && \
    apt-get install -y curl gnupg2 apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev gcc g++ && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

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
