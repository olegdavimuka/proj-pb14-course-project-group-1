from sqlalchemy import Column, String, Integer, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


class Goals(Base):
    __tablename__ = "meet_goals"

    meet_goal_id = Column(Integer, primary_key=True)
    goal = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user_relation = relationship("User", back_populates="meet_goal_relation")
