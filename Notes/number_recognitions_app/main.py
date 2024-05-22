from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch
from torchvision import models, transforms
from PIL import Image
import io

app = FastAPI() # Create an instance of FastAPI, object of FastAPI class

# Load the model
model = models.resnet18(pretrained=True) # pretrained model with 1000 classes for image classification
# pretrained=True means that the model is already trained on ImageNet dataset and we will not modify the weights
model.eval() # Set the model to evaluation mode

# Define the transformation, preprocessing the image
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
# The preprocessing is done in the same way as the model was trained on ImageNet dataset, search internet for the values

# Set up end point
@app.post("/predict/") # End point here is /predict/ ;; handles the POST request
# app.post handles the POST request, which is used to send data to the server to create/update a resource
async def predict(file: UploadFile = File(...)): # This line ensures that the file is uploaded as part of the request, any request without a file will be rejected
    image_data = await file.read()  # Read the image data
    image = Image.open(io.BytesIO(image_data)) # Open the image using PIL library as it is sent as bytes
    image = transform(image).unsqueeze(0) # Apply the transformation sprecified earlier, and add a batch dimension (need to add a batch dimension as the model expects a batch of images)
    # At this point, the image is ready to be sent to the model 
    # The model expects a prediction from the model
    
    with torch.no_grad(): # Disable gradient calculation as we are not training the model
        output = model(image) # Get the output from the model contains the probabilities of each class
        prediction = output.argmax(1).item() # Get the index of the class with the highest probability
        
    return JSONResponse(content={"predictions": prediction}) # Return the prediction as a JSON response
    
    
    