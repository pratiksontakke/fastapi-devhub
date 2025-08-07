# app/api/posts.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostOut
from app.models.post import Post
from app.db.session import SessionLocal

router = APIRouter()

@router.post("/", response_model=PostOut)
def create_post(post_in: PostCreate, db: Session = Depends(SessionLocal)):
    post = Post(**post_in.dict(), owner_id=1)  # hardcoded for now
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/", response_model=list[PostOut])
def get_posts(db: Session = Depends(SessionLocal)):
    return db.query(Post).all()
