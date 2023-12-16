from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy import delete, select

from app.db import async_session
from app.models import Goals, Hobby, User
from app.telegram.filters import DeleteButtons, DeleteProfile

delete_router = Router()


@delete_router.message(Command("delete_profile"))
async def command_delete_handler(message: Message, state: FSMContext) -> None:
    async with async_session() as session:
        result = (await session.execute(select(User).where(User.user_id == message.from_user.id))).all()  # type: ignore
    if not result:
        await message.answer(text="Твій профіль не знайдено.")
    else:
        builder = InlineKeyboardBuilder()
        for button in DeleteButtons:
            builder.button(
                text=button.value,
                callback_data=DeleteProfile(action=button),
            )
            builder.adjust(1, repeat=True)
        await message.answer(text="Дійсно хочеш видалити свій профіль?:", reply_markup=builder.as_markup())


@delete_router.callback_query(DeleteProfile.filter(F.action == DeleteButtons.yes))
async def callback_query_delete_profile(query: CallbackQuery) -> None:
    async with async_session() as session:
        await session.execute(delete(Goals).where(Goals.user_id == query.from_user.id))
        await session.execute(delete(Hobby).where(Hobby.user_id == query.from_user.id))
        await session.execute(delete(User).where(User.user_id == query.from_user.id))
        await session.commit()
    await query.message.answer("Профіль видаленo")  # type: ignore


@delete_router.callback_query(DeleteProfile.filter(F.action == DeleteButtons.no))
async def callback_query_not_delete_profile(query: CallbackQuery) -> None:
    await query.message.answer("Ми раді, що ти залишаєшся з нами 🫂")  # type: ignore
