from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemOut(ItemCreate):
    id: int
    class Config:
        orm_mode = True  # Important for returning ORM objects as JSON
