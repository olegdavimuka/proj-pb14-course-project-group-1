from sqlalchemy import Column, String, Integer, ForeignKey, Float
from .models import Base


class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True)
    reviewed_user_id = Column(Integer)
    review = Column(String)
    meet_rating = Column(Float)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    reviewed_user_id = Column(Integer, ForeignKey('users.user_id'))
