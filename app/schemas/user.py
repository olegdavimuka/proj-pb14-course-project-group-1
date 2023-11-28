from pydantic import BaseModel
from constants import UserStatus


class User(BaseModel):
    user_id: int
    user_name: str
    user_age: int
    user_location: str
    domain: str
    position: str
    photo: bytes
    description: str | None
    status: UserStatus
    raiting: float = 5.0

