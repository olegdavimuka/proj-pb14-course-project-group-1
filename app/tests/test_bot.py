import os
import pytest
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import FSMContext
from aiogram import executor
from dotenv import load_dotenv, find_dotenv
from app.telegram.bot import dp, send_welcome

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")


@pytest.fixture
def bot():
    return Bot(BOT_TOKEN)


def test_send_welcome(bot, monkeypatch):
    monkeypatch.setattr(
        executor, "start_polling", lambda *args, **kwargs: None
    )

    message = types.Message(
        message_id=1,
        chat=types.Chat(id=1, type="private"),
        date=123456789,
        text="/start",
    )

    executor.Dispatcher.set_current(dp)
    executor.Dispatcher.set_current(dp)
    executor.Dispatcher.set_current(dp)

    async def fake_send_welcome(message: Message):
        assert message.text == "/start"
        await send_welcome(message)

    with executor.Dispatcher.current().freeze():
        dp.message_handlers.append(
            types.MessageHandler(send_welcome, commands=["start"])
        )
        dp.message_handlers.append(
            types.MessageHandler(fake_send_welcome, commands=["start"])
        )
        executor.Dispatcher.set_current(dp)
        dp.process_message(message)

    assert message.text == "/start"
    executor.Dispatcher.set_current(dp)

    dp.message_handlers.clear()
