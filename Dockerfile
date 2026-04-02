# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for OpenCV and other libs
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any exact dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Create necessary directories for file uploads and predictions
# and set permissions so the app can write to them
RUN mkdir -p static/uploads static/predictions && \
    chmod 777 static/uploads static/predictions

# Expose port 7860 for Hugging Face Spaces
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
