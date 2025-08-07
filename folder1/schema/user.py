from pydantic import BaseModel
from typing import List
from .post import Post

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_verified: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True