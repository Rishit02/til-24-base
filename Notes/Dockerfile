# Use PyTorch GPU image with Python 3.10 from Google Cloud as the base image
FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/pytorch-gpu.2-2.py310
#Base image is python 3.10 with pytorch from google cloud. This is a pure python image with no additional packages installed. 
#We will install FastAPI, Uvicorn, Pillow, Torchvision, and python-multipart packages in this image.

# Install additional packages
RUN pip install fastapi uvicorn Pillow torchvision python-multipart

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]