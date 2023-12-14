from aiogram import Dispatcher

from .start import form_router as start_router

dp = Dispatcher()
dp.include_router(start_router)
