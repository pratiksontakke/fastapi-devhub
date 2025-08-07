from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    likes: int

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True