from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": f"User {user} has been created!"}
