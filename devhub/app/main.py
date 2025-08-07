# app/main.py
from fastapi import FastAPI
from app.api import auth, posts
from app.db.session import engine
from app.models import user, post

# Create tables (optional, use Alembic in real setup)
user.Base.metadata.create_all(bind=engine)
post.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DevHub API")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
