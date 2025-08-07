# app/schemas/post.py
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    name: str
    email: str
    password: str
    isvarified: bool

    class Config:
        orm_mode = True