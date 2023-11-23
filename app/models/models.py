from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Time, String, Integer, LargeBinary, Float, func, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = Base.metadata


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
    raiting = Column(Float, default=5.0)
    hobbies = relationship("Hobby")
    proposals = relationship("Proposal")
    feedback = relationship("Feedback")
    meet_goals = relationship("Goals")


class Goals(Base):
    __tablename__ = "meet_goals"

    meet_goal_id = Column(Integer, primary_key=True)
    goal = Column(String(20))
    user_id = Column(Integer, ForeignKey('users.user_id'))

class Hobby(Base):
    __tablename__ = "hobbies"

    hobby_id = Column(Integer, primary_key=True)
    hobby = Column(String(20))
    user_id = Column(Integer, ForeignKey('users.user_id'))


class Proposal(Base):
    __tablename__ = "proposals"

    proposal_id = Column(Integer, primary_key=True)
    proposed_user_id = Column(Integer)
    status = Column(String)
    answer_time = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    proposed_user_id = Column(Integer, ForeignKey('users.user_id'))


class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True)
    reviewed_user_id = Column(Integer)
    review = Column(String)
    meet_rating = Column(Float)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    reviewed_user_id = Column(Integer, ForeignKey('users.user_id'))

