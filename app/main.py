from fastapi import FastAPI, HTTPException, Response, status

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

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for existing_user in users:
        if existing_user.user_id == user_id:
            return existing_user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )

@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for index, existing_user in enumerate(users):
        if existing_user.user_id == user_id:
            users.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )