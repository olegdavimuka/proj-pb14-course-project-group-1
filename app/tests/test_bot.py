import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
import pytest
from aiogram import types
from app.telegram.bot import dp, send_welcome


@pytest.mark.asyncio
async def test_send_welcome(mocker):
    user_message = types.Message(
        message_id=1,
        chat=types.Chat(id=1, type="private"),
        from_user=types.User(id=1, is_bot=False, first_name="Test"),
    )

    mock_reply = mocker.patch("aiogram.types.Message.reply")

    await send_welcome(user_message)

    mock_reply.assert_called_once_with("Привiт! Я ваш телеграм-бот.")
