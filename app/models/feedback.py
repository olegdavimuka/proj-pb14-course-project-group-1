from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True)
    review = Column(String)
    meet_rating = Column(Float)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    reviewed_user_id = Column(Integer, ForeignKey("users.user_id"))
    user_relation = relationship("User", back_populates="feedback_relation", foreign_keys=[user_id])
    reviewed_user_relation = relationship(
        "User", back_populates="reviewed_feedback_relation", foreign_keys=[reviewed_user_id]
    )
