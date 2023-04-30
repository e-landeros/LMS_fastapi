from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str
    role: int


# i am setting up a password on create skip for now.
class UserCreate(UserBase):
    ...


# returning a user
class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # handles iterables and converts them to dicts; important that its true
