from collections import defaultdict

from sqlalchemy import Column, Float, Integer, String, select
from sqlalchemy.orm import relationship

from app.db import Base, async_session
from app.models.goals import Goals
from app.models.hobby import Hobby


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    user_name = Column(String(60))
    nickname = Column(String(60))
    user_age = Column(Integer)
    user_location = Column(String(30))
    domain = Column(String)
    position = Column(String)
    photo = Column(String)
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

    @classmethod
    async def get_user_profiles(cls, with_user_id: bool = True, with_photo: bool = True):
        async with async_session() as session:
            result = await session.execute(
                select(User, Goals, Hobby).where(User.user_id == Goals.user_id, User.user_id == Hobby.user_id)
            )
            rows = result.fetchall()
            user_profiles: defaultdict[str, dict[str, str | list[str]]] = defaultdict(lambda: {"hobby": []})
            for user, goals, hobby in rows:
                if with_user_id:
                    user_profiles[user.user_id]["user_id"] = user.user_id
                    user_profiles[user.user_id]["chat_id"] = user.chat_id
                user_profiles[user.user_id]["nickname"] = user.nickname
                user_profiles[user.user_id]["user_age"] = user.user_age
                user_profiles[user.user_id]["user_age"] = user.user_age
                if with_photo:
                    user_profiles[user.user_id]["photo"] = user.photo
                user_profiles[user.user_id]["user_location"] = user.user_location
                user_profiles[user.user_id]["domain"] = user.domain
                user_profiles[user.user_id]["position"] = user.position
                user_profiles[user.user_id]["description"] = user.description
                user_profiles[user.user_id]["goals"] = goals.goal
                user_profiles[user.user_id]["hobby"].append(hobby.hobby)  # type: ignore

        return dict(user_profiles)
