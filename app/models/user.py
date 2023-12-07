from sqlalchemy import Column, Float, Integer, LargeBinary, String
from sqlalchemy.orm import relationship

from app.db import Base


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
    rating = Column(Float, default=5.0)
    hobby_relation = relationship("Hobby", back_populates="user_relation")
    proposals_relation = relationship(
        "Proposal",
        back_populates="user_relation",
        primaryjoin="Proposal.user_id == User.user_id",
        foreign_keys="Proposal.user_id",
    )
    proposed_user_relation = relationship(
        "Proposal",
        back_populates="user_proposed_relation",
        primaryjoin="Proposal.proposed_user_id == User.user_id",
        foreign_keys="Proposal.proposed_user_id",
    )
    feedback_relation = relationship(
        "Feedback",
        back_populates="user_relation",
        primaryjoin="Feedback.user_id == User.user_id",
        foreign_keys="Feedback.user_id",
    )
    reviewed_feedback_relation = relationship(
        "Feedback",
        back_populates="reviewed_user_relation",
        primaryjoin="Feedback.reviewed_user_id == User.user_id",
        foreign_keys="Feedback.reviewed_user_id",
    )
    meet_goal_relation = relationship("Goals", back_populates="user_relation")
