from aiogram import F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery

from app.telegram.routers.utils import show_user_profile

matching_router = Router()


class ProposalCheckApproval(CallbackData, prefix="proposal-check-approval"):
    user_id: int


class ProposalCheckDenial(CallbackData, prefix="proposal-check-denial"):
    user_id: int


@matching_router.callback_query(ProposalCheckApproval.filter(F.user_id))
async def callback_query_delete_approval_profile(query: CallbackQuery, callback_data: ProposalCheckApproval) -> None:
    await show_user_profile(query.message, callback_data.user_id)  # type: ignore


@matching_router.callback_query(ProposalCheckDenial.filter(F.user_id))
async def callback_query_delete_denial_profile(query: CallbackQuery, callback_data: ProposalCheckDenial) -> None:
    await query.message.answer("Добре, тоді нагадаю тобі пізніше")  # type: ignore
