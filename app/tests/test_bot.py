import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)

import unittest
from unittest.mock import patch
from aiogram import types, executor
from app.telegram.bot import dp, send_welcome


class TestYourBot(unittest.TestCase):
    @patch("aiogram.types.Message")
    @patch("aiogram.types.Message.reply")
    async def test_send_welcome(self, mock_reply, mock_message):
        user_message = types.Message(
            message_id=1,
            chat=types.Chat(id=1, type="private"),
            from_user=types.User(id=1, is_bot=False, first_name="Test"),
        )
        await send_welcome(user_message)
        mock_reply.assert_called_once_with("Привiт! Я ваш телеграм-бот.")

    def tearDown(self):
        patch.stopall()


if __name__ == "__main__":
    unittest.main()
