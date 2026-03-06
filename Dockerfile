# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy your app code
COPY app.py .

# Run the app by default
CMD ["python", "app.py"]
