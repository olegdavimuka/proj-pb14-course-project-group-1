from aiogram import Bot
from aiogram.enums import ParseMode

from app.constants import BOT_TOKEN
from app.telegram.routers import dp


async def start_bot():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

    await dp.start_polling(bot)
