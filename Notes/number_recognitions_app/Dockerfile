# Use PyTorch GPU image with Python 3.10 from Google Cloud as the base image
FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/pytorch-gpu.2-2.py310

# Install additional packages
RUN pip install fastapi uvicorn Pillow torchvision python-multipart

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]