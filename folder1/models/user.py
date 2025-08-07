from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from folder1.db.base import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    # user_id = Column(Integer, ForeignKey("users.id"))
    password = Column(String)
    isvarified = Column(Boolean)
