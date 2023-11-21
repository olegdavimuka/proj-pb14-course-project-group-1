import logging
import openai
import os
import requests
import aiogram
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)
GPT_KEY = os.getenv("GPT_KEY")
openai.api_key = GPT_KEY
TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise ValueError("Token not found.")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Example
@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Привiт! Я ваш бот.")

#Example
@dp.message_handler(Command("gpt_request"))
async def handle_gpt_request(message: types.Message) -> None:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Привi, як ти?",
        max_tokens=100
    )
    await message.answer(response['choices'][0]['text'])


if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)