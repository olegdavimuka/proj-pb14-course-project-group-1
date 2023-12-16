from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    name = State()
    age = State()
    photo = State()
    location = State()
    hobbies = State()
    domain = State()
    position = State()
    goals = State()
    description = State()


class Edit(StatesGroup):
    edit_name = State()
    edit_age = State()
    edit_photo = State()
    edit_location = State()
    edit_hobbies = State()
    edit_domain = State()
    edit_position = State()
    edit_goals = State()
    edit_description = State()
