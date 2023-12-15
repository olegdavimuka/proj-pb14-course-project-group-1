from aiogram import Dispatcher

from .show_profile import router as show_router
from .start import form_router as start_router

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(show_router)
