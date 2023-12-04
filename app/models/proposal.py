from sqlalchemy import Column, String, Integer, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


class Proposal(Base):
    __tablename__ = "proposals"

    proposal_id = Column(Integer, primary_key=True)
    proposed_user_id = Column(Integer)
    status = Column(String)
    answer_time = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    proposed_user_id = Column(Integer, ForeignKey("users.user_id"))
    user_relation = relationship("User", back_populates="feedback_relation")
    user_proposed_relation = relationship(
        "User", back_populates="proposed_user_relation"
    )
