# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI application code into the container
COPY main.py /app/

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn prometheus-fastapi-instrumentator

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]