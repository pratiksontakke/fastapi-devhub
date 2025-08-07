# app/schemas/post.py
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    likes: int
    user_id: int

    class Config:
        orm_mode = True