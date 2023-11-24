from sqlalchemy import Column, String, Integer, LargeBinary, Float
from sqlalchemy.orm import relationship
from .models import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(60))
    user_age = Column(Integer)
    user_location = Column(String(30))
    domain = Column(String)
    position = Column(String)
    photo = Column(LargeBinary)
    description = Column(String, nullable=True)
    status = Column(String)
    raiting = Column(Float, default=5.0)
    hobbies = relationship("Hobby")
    proposals = relationship("Proposal")
    feedback = relationship("Feedback")
    meet_goals = relationship("Goals")
