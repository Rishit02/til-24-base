from fastapi import FastAPI

app = FastAPI() # Create an instance of FastAPI, object of FastAPI class
@app.get("/") # Decorator to define the path of the API
# app.get handles the GET request, which is used to request data from a specified resource
# Inside fastAPI/some_path, the function hello() will be executed
def hello():
    return {"message": "Hello, this is the first API with FastAPI!"}


# This is the file which will be executed, so it is the API server
# python -m uvicorn fastapi_hello_world:app --host 0.0.0.0 --port 8000 ;;; to run the server
# http://localhost:8000/ ;;; to access the API
# file name:app ---> the uvicorn looks for the app object in the file
# local is 0.0.0.0 and expose for 8000