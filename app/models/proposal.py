from sqlalchemy import Column, ForeignKey, Integer, String, select
from sqlalchemy.orm import aliased, relationship

from app.db import Base, async_session
from app.models.user import User


class Proposal(Base):
    __tablename__ = "proposals"

    proposal_id = Column(Integer, primary_key=True)
    status = Column(String)
    user_answer_time = Column(Integer)
    proposed_user_answer_time = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    proposed_user_id = Column(Integer, ForeignKey("users.user_id"))
    user_relation = relationship("User", back_populates="proposals_relation", foreign_keys=[user_id])
    user_proposed_relation = relationship(
        "User", back_populates="proposed_user_relation", foreign_keys=[proposed_user_id]
    )

    @classmethod
    async def get_ready_proposals(cls):
        async with async_session() as session:
            proposed_user = aliased(User)

            result = await session.execute(
                select(Proposal, User, proposed_user).where(
                    Proposal.user_answer_time == None,  # noqa: E711
                    Proposal.proposed_user_answer_time == None,  # noqa: E711
                    Proposal.status == None,  # noqa: E711
                    Proposal.user_id == User.user_id,
                    Proposal.proposed_user_id == proposed_user.user_id,
                )
            )
            proposals = result.fetchall()
            for _, user, proposed_user in proposals:
                yield user.user_id, user.chat_id, proposed_user.user_id, proposed_user.chat_id
