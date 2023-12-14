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
