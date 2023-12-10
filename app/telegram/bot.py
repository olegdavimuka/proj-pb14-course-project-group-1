import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from app.config import BOT_TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(self, message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message.from_user:
        await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    else:
        await message.answer("Hello!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    if BOT_TOKEN:
        bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
        await dp.start_polling(bot)
    else:
        logging.error("Bot token is not provided.")


if __name__ == "__main__":
    asyncio.run(main())
