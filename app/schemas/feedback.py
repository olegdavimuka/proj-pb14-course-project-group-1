from pydantic import BaseModel


class Feedback(BaseModel):
    feedback_id: int
    reviewed_user_id: int
    review: str
    meet_rating: float
    user_id: int
