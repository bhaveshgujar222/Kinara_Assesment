
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the ETL script and tests
COPY . .

# Run the ETL application
CMD ["python", "main.py"]
