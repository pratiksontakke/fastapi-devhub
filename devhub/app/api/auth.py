# app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.services.user import create_user, get_user_by_username
from app.core.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from app.api.deps import get_db # <--- IMPORT THE CORRECT DEPENDENCY

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)): # <--- USE get_db
    user = get_user_by_username(db, user_in.username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user_in)

@router.post("/token") 
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): # <--- USE get_db
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}