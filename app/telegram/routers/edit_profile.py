from aiogram import Router, F, Bot  # noqa: I001, F401
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy import select  # noqa: F401

from app.db import async_session  # noqa: F401, I001
from app.models import User
from app.telegram.routers.utils import show_user_profile, get_field_errors
from app.telegram.forms import Edit
from app.telegram.filters import EditProfile, EditButtons  # noqa: F401
from aiogram.fsm.context import FSMContext
from app import schemas


edit_router = Router()


@edit_router.message(Command("edit_profile"))
async def command_edit_handler(message: Message, state: FSMContext) -> None:
    async with async_session() as session:
        result = (await session.execute(select(User).where(User.user_id == message.from_user.id))).all()  # type: ignore
    if not result:
        await message.answer(text="Твій профіль не знайдено. Розпочни його створення з команди /start")
    else:
        await message.answer(text="Твій профіль зараз виглядає так:")
        await show_user_profile(message, message.from_user.id)  # type: ignore
    await state.set_state(Edit.edit_name)
    builder = InlineKeyboardBuilder()
    for button in EditButtons:
        builder.button(
            text=button.value,
            callback_data=EditProfile(action=button),
        )
        builder.adjust(1, repeat=True)
    # inline_markup = InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, selective=True)
    await message.answer(text="Обери що хочеш змінити:", reply_markup=builder.as_markup())


@edit_router.callback_query(EditProfile.filter(F.action == EditButtons.name))
async def callback_query_edit_profile(query: CallbackQuery, state: FSMContext) -> None:
    await query.message.answer("Введи своє нове ім'я:")  # type: ignore
    await state.set_state(Edit.edit_name)


@edit_router.message(Edit.edit_name)
async def edit_profile_name(message: Message, state: FSMContext):
    if get_field_errors(schemas.User, {"user_name": message.text}, "user_name") or not message.text:
        await message.answer("Нажаль щось пішло не так, давай спробуємо ще раз. Введи своє ім'я:")
    else:
        async with async_session() as session:
            result = await session.execute(select(User).where(User.user_id == message.from_user.id))  # type: ignore
            user = result.scalars().one()
            user.user_name = message.text  # type: ignore
            await session.commit()
        await state.clear()
        await message.answer(text="Зміни збережено 🪄")


# Реалізовано тільки для зміни імені, потрібно додати пізніше
