import asyncio
import pytest
from aiogram import types
from app.telegram.bot import main, dp


@pytest.mark.asyncio
@pytest.mark.timeout(1)
async def test_command_start_handler():
    message = types.Message(
        chat=types.Chat(id=123, type="private"),
        from_user=types.User(id=456, is_bot=False, username="test_user", full_name="Test User"),
        date=123456789,
        text="/start",
    )

    dp.update_process_timeouts = 0.1

    with pytest.raises(asyncio.TimeoutError):
        await asyncio.gather(
            main(),
            dp.message_handlers.handlers[0][0](message),
        )


@pytest.mark.asyncio
@pytest.mark.timeout(1)
async def test_echo_handler():
    message = types.Message(
        chat=types.Chat(id=123, type="private"),
        from_user=types.User(id=456, is_bot=False, username="test_user", full_name="Test User"),
        date=123456789,
        text="Hello, bot!",
    )

    dp.update_process_timeouts = 0.1

    with pytest.raises(asyncio.TimeoutError):
        await asyncio.gather(
            main(),
            dp.message_handlers.handlers[None][0](message),
        )
