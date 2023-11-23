from pydantic import BaseModel


class Hobby(BaseModel):
    hobby_id: int
    hobby: str
    user_id: int
