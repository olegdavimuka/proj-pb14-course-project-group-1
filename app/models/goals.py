from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Goals(Base):
    __tablename__ = "meet_goals"

    meet_goal_id = Column(Integer, primary_key=True)
    goal = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user_relation = relationship("User", back_populates="meet_goal_relation")
