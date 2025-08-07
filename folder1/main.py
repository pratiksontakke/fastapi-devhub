from fastapi import FastAPI
from folder1.routers import user, post
from folder1.db.base import Base
from folder1.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(post.router, prefix="/posts", tags=["posts"])