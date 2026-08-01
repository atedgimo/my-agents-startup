# Dockerfile
# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies needed for some packages (if any)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install Python dependencies first (for better caching)
COPY src/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application source code
COPY src/backend /app/src/backend
COPY src/frontend /app/src/frontend

# Expose the port Uvicorn will run on
EXPOSE 8000

# Command to run the application:
# We use a combined startup script or command that runs both the API and serves static files.
# Since FastAPI can serve static content, we'll keep it simple with uvicorn.
CMD ["uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "8000"]