from sqlalchemy import Column, String, Integer, ForeignKey
from .base import Base


class Proposal(Base):
    __tablename__ = "proposals"

    proposal_id = Column(Integer, primary_key=True)
    proposed_user_id = Column(Integer)
    status = Column(String)
    answer_time = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    proposed_user_id = Column(Integer, ForeignKey("users.user_id"))
