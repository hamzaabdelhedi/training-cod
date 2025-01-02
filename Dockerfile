
# Stage 1: Build the application
FROM python:3.12-slim AS builder

# Set environment variables to avoid writing .pyc files and buffer logs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies needed for building (such as build tools and libraries)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Create a smaller runtime image
FROM python:3.12-slim AS runtime

# Set environment variables to avoid writing .pyc files and buffer logs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
    