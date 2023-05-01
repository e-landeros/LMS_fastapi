from typing import List
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.users import User, UserCreate
from api.utils.users import get_users, get_user_by_email, create_user, get_user

# similar to blueprints in flask, set up a router
router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


# @router.post("/users")
# async def create_new_user(user: User):
#     users.append(user)
#     return {"message": f"User {user} has been created!"}
#
#
# @router.get("/users/{id}")
# async def read_user(id: int):
#     return {"user": users[id]}
