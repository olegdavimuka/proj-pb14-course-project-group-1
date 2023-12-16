from aiogram import Dispatcher

from .delete_profile import delete_router
from .edit_profile import edit_router
from .matching import matching_router
from .show_profile import show_router
from .start import form_router as start_router

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(show_router)
dp.include_router(edit_router)
dp.include_router(delete_router)
dp.include_router(matching_router)
