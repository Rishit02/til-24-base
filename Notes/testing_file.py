import requests

# Set the URL for the API
url = "http://localhost:8000/predict/"

# Path to the image file
image_path = "cat.jpeg"

# Open the image file
with open(image_path, "rb") as image_file:
    #Set up payload a dictionary with the key "file" and the value as the image file
    files = {'file': (image_path, image_file, 'image/jpeg')} # this line reads the image file and sets the content type to image/jpeg
    # Send the POST request to the API,
    response = requests.post(url, files=files) # this line sends the request to the API with the image file

# Print the response
print(response.json())