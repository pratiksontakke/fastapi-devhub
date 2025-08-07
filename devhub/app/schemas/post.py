# app/schemas/post.py
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(PostCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
