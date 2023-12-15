from aiogram import Router, html, Dispatcher, Bot, types  # noqa: I001, F401
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton  # noqa: F401
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.logs import logger  # noqa: F401
from app.constants import CITIES, DOMAINS, GOALS, UserStatus, HOBBIES  # noqa: F401
from app.telegram.forms import Form
from aiogram.fsm.context import FSMContext
from app.models import User, Goals, Hobby  # noqa: F401
from app import schemas
from app.db import async_session
import aiogram.utils  # noqa: F401
from aiogram.types import CallbackQuery
from sqlalchemy import select  # noqa: F401


from app.telegram.routers.utils import show_user_profile, get_field_errors

form_router = Router()


@form_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    async with async_session() as session:
        result = (await session.execute(select(User).where(User.user_id == message.from_user.id))).all()  # type: ignore
    if not result:
        await state.set_state(Form.name)
        await message.answer(
            "Почнімо створення анкети. Введи своє ім'я:",
            reply_markup=ReplyKeyboardRemove(),
        )
    else:
        await message.answer(text="З повененням! \nБажаєш переглянути свій профіль? Тисни /show_profile ")


@form_router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    if get_field_errors(schemas.User, {"user_name": message.text}, "user_name"):
        await message.answer("Нажаль щось пішло не так, давай спробуємо ще раз. Введи своє ім'я:")
    else:
        await state.update_data(name=message.text)
        await state.set_state(Form.age)
        await message.answer(
            f"Приємно познайомитись, {message.text}!\nВкажи свій вік:",
            reply_markup=ReplyKeyboardRemove(),
        )


@form_router.message(Form.age)
async def process_age(message: Message, state: FSMContext) -> None:
    if get_field_errors(schemas.User, {"user_age": message.text}, "user_age"):
        await message.answer("Ой-ой, щось дивне, давай спробуємо ще раз. Вкажи свій вік:")
    else:
        await state.update_data(age=message.text)
        await state.set_state(Form.photo)
        await message.answer("Чудово, тепер надішли своє фото:")


@form_router.message(Form.photo)
async def process_photo(message: Message, state: FSMContext) -> None:
    if (photo_obj := message.photo) and message._bot:
        await state.update_data(photo=photo_obj[-1].file_id)
        await state.set_state(Form.location)
        keyboard = [[InlineKeyboardButton(text=city, callback_data=city)] for city in CITIES]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, selective=True)
        builder = InlineKeyboardBuilder()
        builder.attach(InlineKeyboardBuilder.from_markup(inline_markup))
        builder.adjust(3, repeat=True)
        await message.answer("Гарне фото, обери своє місто зі списку:", reply_markup=builder.as_markup())
        return None
    await message.answer("Потрібне фото, спробуй ще раз")


@form_router.callback_query(Form.location)
async def process_location(query: CallbackQuery, state: FSMContext) -> None:
    if not query.message:
        # Reason behind absence of message is unclear, maybe some rare cases like deleted chat or outdated message
        logger.error(f"There's no message in query(process_hobbies) {query}")
        return None
    await state.update_data(location=query.data)
    await state.set_state(Form.hobbies)
    keyboard = [[InlineKeyboardButton(text=hobby, callback_data=hobby)] for hobby in HOBBIES]
    inline_markup = InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, selective=True)
    builder = InlineKeyboardBuilder()
    builder.attach(InlineKeyboardBuilder.from_markup(inline_markup))
    builder.adjust(2, repeat=True)
    await query.message.answer("Знайди тут свої хобі:", reply_markup=builder.as_markup())


@form_router.callback_query(Form.hobbies)
async def process_hobbies(query: CallbackQuery, state: FSMContext) -> None:
    if not query.message:
        # Reason behind absence of message is unclear
        logger.error(f"There's no message in query(process_hobbies) {query}")
        return None
    selected_hobbies = (await state.get_data()).get("hobbies", [])
    hobby = query.data

    if hobby == "Це все":
        ...
    elif hobby not in selected_hobbies:
        selected_hobbies.append(hobby)
    else:
        selected_hobbies.remove(hobby)

    await state.update_data(hobbies=selected_hobbies)

    if len(selected_hobbies) >= 1 and hobby == "Це все":
        keyboard = [[InlineKeyboardButton(text=domain, callback_data=domain)] for domain in DOMAINS]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, selective=True)
        builder = InlineKeyboardBuilder()
        builder.attach(InlineKeyboardBuilder.from_markup(inline_markup))
        builder.adjust(2, repeat=True)
        await state.set_state(Form.domain)
        await query.answer()
        await query.message.answer("Записано, обери сферу в якій працюєш: ", reply_markup=builder.as_markup())  # type: ignore
    else:
        keyboard = [
            [InlineKeyboardButton(text=f"✅ {hobby}" if hobby in selected_hobbies else hobby, callback_data=hobby)]
            for hobby in HOBBIES
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, selective=True)
        builder = InlineKeyboardBuilder()
        builder.attach(InlineKeyboardBuilder.from_markup(inline_markup))
        builder.adjust(2, repeat=True)
        await query.message.edit_reply_markup(reply_markup=builder.as_markup())


@form_router.callback_query(Form.domain)
async def process_domain(query: CallbackQuery, state: FSMContext) -> None:
    if not query.message:
        # Reason behind absence of message is unclear, maybe some rare cases like deleted chat or outdated message
        logger.error(f"There's no message in query(process_hobbies) {query}")
        return None
    await state.update_data(domain=query.data)
    await state.set_state(Form.position)
    await query.message.answer("Є, вкажи свою посаду:")


@form_router.message(Form.position)
async def process_position(message: Message, state: FSMContext) -> None:
    await state.update_data(position=message.text)
    await state.set_state(Form.goals)
    keyboard = [[InlineKeyboardButton(text=goal, callback_data=goal)] for goal in GOALS]
    inline_markup = InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True, selective=True)
    builder = InlineKeyboardBuilder()
    builder.attach(InlineKeyboardBuilder.from_markup(inline_markup))
    builder.adjust(2, repeat=True)
    await message.answer("Які в тебе цілі?", reply_markup=builder.as_markup())


@form_router.callback_query(Form.goals)
async def process_goals(query: CallbackQuery, state: FSMContext) -> None:
    if not query.message:
        # Reason behind absence of message is unclear, maybe some rare cases like deleted chat or outdated message
        logger.error(f"There's no message in query(process_hobbies) {query}")
        return None
    await state.update_data(goals=query.data)
    await state.set_state(Form.description)
    await query.message.answer("Майже завершили, напиши ще декілька слів про себе", reply_markup=ReplyKeyboardRemove())


@form_router.message(Form.description)
async def process_registration_end(message: Message, state: FSMContext) -> None:
    if not message.from_user:
        logger.error(f"There's no user id from attached to message {message}")
        return None
    await state.update_data(description=message.text)
    user_data = await state.get_data()
    async with async_session() as session:
        user_info = User(
            user_id=message.from_user.id,
            user_name=user_data["name"],
            user_age=int(user_data["age"]),
            domain=user_data["domain"],
            user_location=user_data["location"],
            position=user_data["position"],
            photo=user_data["photo"],
            description=user_data["description"],
            status=UserStatus.ACTIVE.value,
        )
        session.add(user_info)
        for hobby in user_data["hobbies"]:
            hobbies = Hobby(hobby=hobby, user_id=message.from_user.id)
            session.add(hobbies)
        meet_goals = Goals(goal=user_data["goals"], user_id=message.from_user.id)
        session.add(meet_goals)
        await session.commit()
        await show_user_profile(message, message.from_user.id)
    await state.clear()
    await message.answer(
        "<b>Твій профіль готовий ✨ </b>",
        parse_mode=ParseMode.HTML,
    )
    await show_user_profile(message, message.from_user.id)
