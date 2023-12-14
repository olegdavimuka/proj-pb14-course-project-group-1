from re import fullmatch

from pydantic import BaseModel, field_validator

from app.constants import UserStatus


class User(BaseModel):
    user_id: int
    user_name: str
    user_age: int
    user_location: str
    domain: str
    position: str
    photo: str
    description: str | None
    status: UserStatus
    rating: float = 5.0

    @field_validator("user_name")
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if not fullmatch("^[A-Za-zА-Яа-яіІїЇґҐ ]+$", v):
            raise ValueError("Must contain only letters")
        return v

    @field_validator("user_age")
    @classmethod
    def age_must_contain_space(cls, v: int) -> int:
        if not (18 <= v <= 100):
            raise ValueError("Must be bigger than 18 and less than 100")
        return v
