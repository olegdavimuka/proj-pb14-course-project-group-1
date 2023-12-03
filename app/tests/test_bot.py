import sys
import os
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from aiogram import types
from app.telegram.bot import send_welcome


class TestSendWelcome(unittest.IsolatedAsyncioTestCase):
    @patch("aiogram.utils.executor", MagicMock())
    async def test_send_welcome(self):
        message = types.Message(
            message_id=1,
            chat=types.Chat(id=123),
            from_user=types.User(id=456),
            date=123456789,
            text="/start",
        )
        mock_reply = AsyncMock()
        message.reply = mock_reply
        await send_welcome(message)
        mock_reply.assert_called_once_with("Привiт! Я ваш телеграм-бот.")


if __name__ == "__main__":
    unittest.main()
