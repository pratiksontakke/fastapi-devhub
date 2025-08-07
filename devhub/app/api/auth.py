# app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.services.user import create_user, get_user_by_username
from app.core.security import verify_password, create_access_token
from app.db.session import SessionLocal

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(SessionLocal)):
    user = get_user_by_username(db, user_in.username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user_in)

@router.post("/login")
def login(user_in: UserCreate, db: Session = Depends(SessionLocal)):
    user = get_user_by_username(db, user_in.username)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
