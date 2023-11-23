from sqlalchemy import Column, String, Integer, ForeignKey
from .models import Base


class Hobby(Base):
    __tablename__ = "hobbies"

    hobby_id = Column(Integer, primary_key=True)
    hobby = Column(String(20))
    user_id = Column(Integer, ForeignKey('users.user_id'))
