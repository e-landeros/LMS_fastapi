from typing import Optional, List
from pydantic import BaseModel
import fastapi

# similar to blueprints in flask, set up a router
router = fastapi.APIRouter()


users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": f"User {user} has been created!"}


@router.get("/users/{id}")
async def get_user(id: int):
    return {"user": users[id]}
