import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user creates a command /start
    """
    await message.reply("Привiт! Я ваш телеграм-бот.")


if __name__ == "__main__":
    # Bot start
    executor.start_polling(dp, skip_updates=True)
