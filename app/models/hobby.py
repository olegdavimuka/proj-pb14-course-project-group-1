from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Hobby(Base):
    __tablename__ = "hobbies"

    hobby_id = Column(Integer, primary_key=True)
    hobby = Column(String(30))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user_relation = relationship("User", back_populates="hobby_relation")
