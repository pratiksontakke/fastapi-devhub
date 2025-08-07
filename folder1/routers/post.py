from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from folder1.db.session import SessionLocal
from folder1.models.post import Post as PostModel
from folder1.schema.post import Post, PostCreate
from folder1.models.user import User as UserModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Post)
def create_post_for_user(user_id: int, post: PostCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_post = PostModel(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = db.query(PostModel).offset(skip).limit(limit).all()
    return posts

@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post