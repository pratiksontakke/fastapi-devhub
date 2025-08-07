from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from folder1.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_verified = Column(Boolean, default=False)

    posts = relationship("Post", back_populates="owner")