from aiogram import Router  # noqa: I001, F401
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select  # noqa: F401

from app.db import async_session  # noqa: F401, I001
from app.models import User
from app.telegram.routers.utils import show_user_profile

router = Router()


@router.message(Command("show_profile"))
async def command_show_handler(message: Message) -> None:
    async with async_session() as session:
        result = (await session.execute(select(User).where(User.user_id == message.from_user.id))).all()  # type: ignore
    if not result:
        await message.answer(text="Твій профіль не знайдено. Розпочни його створення з команди /start")
    else:
        await message.answer(text="Твій профіль:")
        await show_user_profile(message, message.from_user.id)  # type: ignore
