# Base Image
FROM python:3.12-slim

# Setting user as root to complete the necessary installations
USER root
RUN apt-get update --fix-missing && \
    apt-get install -y --fix-missing  build-essential  curl && \
    rm -rf /var/lib/apt/lists/*

# Copy the content of the local app directory to the container at /app
COPY ./app /app
COPY ./docker-entrypoint.sh /
COPY ./requirements.txt /

# Set the working directory as app directory, providing proper permissions, and installing the dependencies
WORKDIR /
ENV PYTHONPATH=/
RUN chmod +x /docker-entrypoint.sh && \
    pip install --no-cache-dir -r requirements.txt && \
    chmod -R 777 /app

# Expose the port the app runs on
USER 1001
EXPOSE 5000
# Run the application
ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]