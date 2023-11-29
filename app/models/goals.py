from sqlalchemy import Column, String, Integer, ForeignKey
from .base import Base


class Goals(Base):
    __tablename__ = "meet_goals"

    meet_goal_id = Column(Integer, primary_key=True)
    goal = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.user_id"))
