import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.constants import BOT_TOKEN
from app.models import Proposal
from app.telegram.routers import dp
from app.telegram.routers.matching import ProposalCheckApproval, ProposalCheckDenial


def create_bot():
    return Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)


async def start_bot():
    await asyncio.create_task(dp.start_polling(create_bot()))


async def send_proposals():
    bot = create_bot()
    async for user_id, user_chat_id, proposed_user_id, proposed_user_chat_id in Proposal.get_ready_proposals():
        builder = InlineKeyboardBuilder()
        builder.button(text="Так, звичайно!", callback_data=ProposalCheckApproval(user_id=proposed_user_id).pack())
        builder.button(text="Ні, іншим разом", callback_data=ProposalCheckDenial(user_id=proposed_user_id).pack())
        builder.adjust(2, repeat=True)
        await bot.send_message(
            user_chat_id,
            "Привіт! Я знайшов тобі потенційного партнера для зустрічі. Бажаєш переглянути профіль?",
            reply_markup=builder.as_markup(),
        )
        builder = InlineKeyboardBuilder()
        builder.button(text="Так, звичайно!", callback_data=ProposalCheckApproval(user_id=user_id).pack())
        builder.button(text="Ні, іншим разом", callback_data=ProposalCheckDenial(user_id=user_id).pack())
        builder.adjust(2, repeat=True)
        await bot.send_message(
            proposed_user_chat_id,
            "Привіт! Я знайшов тобі потенційного партнера для зустрічі. Бажаєш поглянути на профіль?",
            reply_markup=builder.as_markup(),
        )
