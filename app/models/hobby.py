from sqlalchemy import Column, String, Integer, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


class Hobby(Base):
    __tablename__ = "hobbies"

    hobby_id = Column(Integer, primary_key=True)
    hobby = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user_relation = relationship("User", back_populates="hobby_relation")
