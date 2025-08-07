# from typing import Optional
# from fastapi import Body, FastAPI, Header, Path, Query
# from fastapi.responses import RedirectResponse
# from pydantic import BaseModel


# app = FastAPI()

# items = [
#     {   "item_id": 1,
#         "name": "Foo",
#         "description": "The Foo fighters",
#         "price": 42.0
#     },
#     {   "item_id": 2,
#         "name": "Bar",
#         "description": "The Bar fighters",
#         "price": 42.0
#     }, 
#     {   "item_id": 3,
#         "name": "Baz",
#         "description": "The Baz fighters",
#         "price": 42.0
#     },
#     {   "item_id": 4,
#         "name": "Baz",
#         "description": "The Baz fighters",
#         "price": 42.0
#     }
# ]

# class Item(BaseModel):
#     name: str
#     description: str = "Pratik is cleaver"
#     price: float


    
# @app.get("/")
# def redirect_to_docs():
#     return RedirectResponse(url="/docs")

# # Path param
# @app.get("/items/{item_id}")
# def read_item(item_id: int = Path(..., description="Item ID from the path")):
#     for item in items:
#         if item["item_id"] == item_id:
#             return item
#     return {"message": "Item not found"}

# # Query param
# @app.get("/items")
# def get_item(search: str = Query(..., description="Keyword to search")):
#     for item in items:
#         if item["name"] == search:
#             return item
#     return {"message": "Item not found"}

# # Header param
# @app.get("/header-check")
# def get_header(x_token: str = Header(..., description="Token from headers")):
#     return {"header_token": x_token}

# @app.post("/submit")
# def submit_user(item: Item = Body(..., description="User info in body")):
#     return {"body_received": item}  


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from practise import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)  # create tables if not exist

app = FastAPI()

# Dependency to get DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/{item_id}", response_model=schemas.ItemOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
