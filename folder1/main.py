
from fastapi import Body, Depends, FastAPI
from sqlalchemy.orm import Session

# from folder1.db.session import SessionLocal
from folder1.db.session import SessionLocal
from folder1.models.post import Post
from folder1.models.user import User

app = FastAPI()

# Dependency to get DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/users")
def add_user(user: User, db: Session = Depends(get_db)):
    db_user = User(user.name, user.email, user.password, user.isvarified)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/post")
def get_all_post(post: Post, db: Session = Depends(get_db)):
    # return db.query(post).filter(models.Item.id == item_id).first()
    return db.query(Post).all()

@app.get("/post/{user_id}")
def get_post_by_userId(user_id: int, db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.user_id == user_id)

@app.post("/post")
def add_post(post: Post, db: Session = Depends(get_db)):
    db_post = Post(post.user_id, post.title, post.likes, post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
