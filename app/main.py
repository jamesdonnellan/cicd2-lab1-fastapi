from fastapi import FastAPI

# Creating the FastAPI Application
app = FastAPI(title="Lab 1 - FastAPI User API")

# Creating the FastAPI Application Objects
@app.get("/health")
# Tells FastAPI to run when the browser sends GET request to the /health endpoint
def health():
    return {"status": "ok"} 

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"} 
