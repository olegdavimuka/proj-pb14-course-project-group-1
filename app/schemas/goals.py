from pydantic import BaseModel


class Goals(BaseModel):
    meet_goal_id: int
    goal: str
    user_id: int
