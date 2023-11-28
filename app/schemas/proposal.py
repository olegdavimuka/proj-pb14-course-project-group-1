from pydantic import BaseModel


class Proposal(BaseModel):
    proposal_id: int
    proposed_user_id: int
    status: str
    answer_time: int
    user_id: int
