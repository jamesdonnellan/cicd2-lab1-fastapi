from fastapi import FastAPI, HTTPException, status

from app.schemas import UserCreate

# Creating the FastAPI Application
app = FastAPI(title="Lab 1 - FastAPI User API")

users: list[UserCreate] = []

# Creating the FastAPI Application Objects
@app.get("/health")
# Tells FastAPI to run when the browser sends GET request to the /health endpoint
def health():
    return {"status": "ok"} 

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"} 

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(new_user: UserCreate):
    for existing_user in users:
        if existing_user.user_id == new_user.user_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this user_id already exists",
            )
    users.append(new_user)
    return new_user