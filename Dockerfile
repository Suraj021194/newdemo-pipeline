# Use official Python image

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependecies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY app code
COPY . .

# Set environment variable (optional)
ENV APP_VERSION=${APP_VERSION}

# RUN the app
CMD ["python", "app.py"]
 
