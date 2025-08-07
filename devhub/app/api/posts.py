# app/api/posts.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostOut
from app.models.post import Post
from app.models.user import User  # <--- IMPORT THE USER MODEL FOR TYPE HINTING
from app.api.deps import get_db, get_current_user # <--- IMPORT get_current_user

router = APIRouter()

@router.post("/", response_model=PostOut)
def create_post(
    post_in: PostCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) # <--- ADD THIS DEPENDENCY
):
    # Use the logged-in user's ID instead of a hardcoded value
    post = Post(**post_in.dict(), owner_id=current_user.id) # <--- USE THE REAL USER ID
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

# The GET endpoint can remain public for anyone to see posts
@router.get("/", response_model=list[PostOut])
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

