from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from folder1.db.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    likes = Column(Integer)
    # owner = relationship("User")
