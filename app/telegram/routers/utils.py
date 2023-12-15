from aiogram.enums import ParseMode
from aiogram.types import Message
from sqlalchemy import select

from app.db import async_session  # noqa: F401, I001
from app.models import Goals, Hobby, User  # noqa: F401


async def show_user_profile(message: Message, user_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(User, Goals, Hobby).where(
                User.user_id == user_id, User.user_id == Goals.user_id, User.user_id == Hobby.user_id
            )
        )
        rows = result.fetchall()
        user_data: dict[str, str | list[str]] = {"hobby": []}
        for user, goals, hobby in rows:
            user_data["user_id"] = user.user_id
            user_data["user_name"] = user.user_name
            user_data["user_age"] = user.user_age
            user_data["photo"] = user.photo
            user_data["user_location"] = user.user_location
            user_data["domain"] = user.domain
            user_data["position"] = user.position
            user_data["description"] = user.description
            user_data["goals"] = goals.goal
            user_data["hobby"].append(hobby.hobby)  # type: ignore

    await message._bot.send_photo(message.chat.id, user_data["photo"])  # type: ignore
    await message.answer(
        f"<b>Ім'я:</b> {user_data['user_name']}\n"
        f"<b>Вік:</b> {user_data['user_age']}\n"
        f"<b>Місто:</b> {user_data['user_location']}\n"
        f"<b>Сфера діяльності:</b> {user_data['domain']}\n"
        f"<b>Посада:</b> {user_data['position']}\n"
        f"<b>Хобі:</b> {', '.join(user_data['hobby'])}\n"
        f"<b>Цілі:</b> {user_data['goals']}\n"
        f"<b>Про себе:</b> {user_data['description']}",
        parse_mode=ParseMode.HTML,
    )
    return user_data
