from enum import Enum

from aiogram.filters.callback_data import CallbackData


class EditButtons(str, Enum):
    name = "Ім'я"
    age = "Вік"
    location = "Місто"
    domain = "Сфера діяльності"
    position = "Посада"
    hobby = "Хобі"
    goals = "Цілі"
    description = "Про себе"
    edit_all = "Переписати все"


class EditProfile(CallbackData, prefix="edit"):
    action: EditButtons
    # chat_id: int
    # user_id: int


class DeleteButtons(str, Enum):
    yes = "ТАК"
    no = "НІ"


class DeleteProfile(CallbackData, prefix="delete"):
    action: DeleteButtons
