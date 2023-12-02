from sqlalchemy import Column, String, Integer, LargeBinary, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from .models import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(String(60))
    user_born_year = Column(Integer)
    user_location_latitude = Column(Float)
    user_location_longitude = Column(Float)
    domain = Column(String)
    position = Column(String)
    photo = Column(LargeBinary)
    description = Column(String, nullable=True)
    status = Column(Boolean)
    raiting = Column(Float, default=5.0)
    hobbies = relationship("Hobby")
    proposals = relationship("Proposal")
    feedback = relationship("Feedback")
    meet_goals = relationship("Goals")