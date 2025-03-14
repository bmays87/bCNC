# Use an official Python base image for ARM architecture
FROM python:3.10-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port if necessary (e.g., 5000 for Flask apps)
EXPOSE 8080

# Command to run your application
CMD ["python", "bCNC/__main__.py"]
